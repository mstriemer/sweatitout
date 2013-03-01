import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, session, abort
from database import db_session
import stripe

from models import Course, Registration, RegistrationCharge, RegistrationForm
from courses import courses, current_courses, old_courses

app = Flask(__name__)

production_env = os.environ.get('APP_ENV', None) == 'production'
if production_env:
    stripe.api_key = os.environ['STRIPE_SECRET_KEY']
    stripe_public_key = os.environ['STRIPE_PUBLIC_KEY']
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    ADMINS = ['mstriemer@gmail.com']
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(
            ('smtp.gmail.com', 587),
            'admin@sweatitoutfit.com',
            ADMINS,
            '[Sweat It Out][Error] An Error Occurred',
            ('admin@sweatitoutfit.com', os.environ['ERROR_SMTP_PASSWORD']),
            ()
        )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
else:
    stripe.api_key = 'sk_test_q6yiThbRguk12pWKh0qlRsLn'
    stripe_public_key = 'pk_test_Mj84H94tNmV6zx7cSCBH2VUQ'
    app.secret_key = 'a0s9fa09sfj01h389gef981g38fgq32f23f93'

def find_card(token):
    if token:
        return stripe.Token.retrieve(token)['card']
    else:
        return None

def charge_registration(registration):
    try:
        stripe_charge = stripe.Charge.create(
                amount=registration.cost_in_cents,
                currency="cad",
                card=registration.stripe_card_token,
                description="{course_name} for {email} - {code}".format(
                    course_name=registration.course_slug,
                    email=registration.email,
                    code=registration.code))
        charge = RegistrationCharge(
                registration_id=registration.id,
                stripe_charge_token=stripe_charge.id,
                paid=stripe_charge['paid'],
                last4=stripe_charge['card']['last4'],
                card_type=stripe_charge['card']['type'],
                currency=stripe_charge['currency'],
                amount=stripe_charge['amount'],
                fee=stripe_charge['fee'],
                charge_time=datetime.fromtimestamp(stripe_charge['created']))
    except stripe.CardError as error:
        charge = RegistrationCharge(
                registration_id=registration.id,
                paid=False,
                error_code=error.code)
    return charge

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html", page_title="Instructors")

def render_group_fitness(course=None, form=None, card=None,
        current_courses=current_courses):
    make_form = lambda c: RegistrationForm(course_slug=c.slug, instance=c)
    courses = []
    for c in current_courses:
        if c == course:
            courses.append((course, form))
        else:
            courses.append((c, make_form(c)))
    return render_template("group_fitness.html", courses=courses, card=card,
            page_title="Group Fitness")

@app.route("/group-fitness")
def group_fitness():
    return render_group_fitness()

@app.route("/group-fitness/<slug>/register")
def group_fitness_registration(slug):
    try:
        course = find_course(slug)
    except ValueError:
        return abort(404)
    form = RegistrationForm(course_slug=course.slug, instance=course)
    form.active = True
    return render_group_fitness(course, form, current_courses=[course])

@app.route("/group-fitness/<slug>/register", methods=["POST"])
def sign_up(slug):
    try:
        course = find_course(slug)
    except ValueError:
        return abort(404)
    form = RegistrationForm(
            course_slug=course.slug,
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            phone=request.form['phone'],
            payment_type=request.form.get('payment_type', ''),
            paypal_email=request.form.get('paypal_email', ''),
            attendance=request.form.get('attendance', ''),
            instance=course,
            stripe_card_token=request.form.get('stripe_card_token', ''),
    )
    if form.valid():
        registration = form.build()
        db_session.add(registration)
        db_session.commit()
        if registration.payment_type == 'stripe':
            charge = charge_registration(registration)
            db_session.add(charge)
            db_session.commit()
        session['registration_id'] = registration.id
        return redirect("/thank-you")
    else:
        form.active = True
        card = find_card(request.form.get('stripe_card_token', None))
        return render_group_fitness(course, form, card, [course])

@app.route("/thank-you")
def thank_you():
    if 'registration_id' in session:
        registration = db_session.query(Registration).filter_by(
                id=session['registration_id']).one()
        course = find_course(registration.course_slug)
        card = find_card(registration.stripe_card_token)
        del session['registration_id']
        return render_template("thank_you.html", registration=registration,
                course=course, page_title="Thank You", card=card)
    else:
        return redirect("/group-fitness")

@app.route("/explode-all-pretty-like")
def explode_all_pretty_like():
    raise TestError("This error was triggered manually")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title="Hmmmmm"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', page_title="Uh oh"), 500


@app.teardown_request
def shutdown_session(exception=None):
        db_session.remove()

@app.context_processor
def inject_stripe_public_key():
    return {'stripe_public_key': stripe_public_key}

@app.context_processor
def inject_google_analytics():
    return {'use_google_analytics': production_env}

@app.context_processor
def inject_secure_host():
    if os.environ.get('DISABLE_SSL'):
        return {}
    else:
        return {'secure_host': 'https://localhost:5000'}

@app.template_filter('currency')
def currency_filter(currency):
    return '${:.2f} CAD'.format(currency)

def find_course(slug):
    for c in courses:
        if c.slug == slug:
            return c
    raise ValueError('could not find course {}'.format(slug))


class TestError(RuntimeError):
    pass
