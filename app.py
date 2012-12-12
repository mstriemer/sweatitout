import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, session
from database import db_session
import stripe

from models import Course, Registration, RegistrationCharge, RegistrationForm

app = Flask(__name__)

production_env = os.environ.get('APP_ENV', None) == 'production'
if production_env:
    stripe.api_key = os.environ['STRIPE_SECRET_KEY']
    stripe_public_key = os.environ['STRIPE_PUBLIC_KEY']
    app.secret_key = os.environ['FLASK_SECRET_KEY']
else:
    stripe.api_key = 'sk_test_q6yiThbRguk12pWKh0qlRsLn'
    stripe_public_key = 'pk_test_Mj84H94tNmV6zx7cSCBH2VUQ'
    app.secret_key = 'a0s9fa09sfj01h389gef981g38fgq32f23f93'

boot_camp_cost = 12320
boot_camp = Course(
        "new-year-2013",
        "New Year's Resolution Bootcamp",
        "Kickstart your new year's resolution with Sweat It Out Fitness's bootcamp. Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
        ["Mondays", "Thursdays"],
        "January 4th",
        "March 27th, 2013",
        "8:45",
        "9:45pm",
        "Revive Fitness Sage Creek",
        "$110 + tax is $123.20 CAD",
        )

def find_card(token):
    if token:
        return stripe.Token.retrieve(token)['card']
    else:
        return None

def charge_registration(registration, amount):
    try:
        stripe_charge = stripe.Charge.create(
                amount=amount,
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

@app.route("/group-fitness")
def group_fitness():
    form = RegistrationForm(course_slug=boot_camp.slug)
    return render_template("group_fitness.html", form=form, course=boot_camp,
            page_title="Group Fitness")

@app.route("/new-year-2013/register")
def redirect_to_group_fitness():
    return redirect("/group-fitness")

@app.route("/new-year-2013/register", methods=["POST"])
def sign_up():
    form = RegistrationForm(
            course_slug=boot_camp.slug,
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            phone=request.form['phone'],
            payment_type=request.form.get('payment_type', ''),
            paypal_email=request.form.get('paypal_email', ''),
            stripe_card_token=request.form.get('stripe_card_token', ''),
    )
    if form.valid():
        registration = form.build()
        db_session.add(registration)
        db_session.commit()
        if registration.payment_type == 'stripe':
            charge = charge_registration(registration, boot_camp_cost)
            db_session.add(charge)
            db_session.commit()
        session['registration_id'] = registration.id
        return redirect("/thank-you")
    else:
        card = find_card(request.form.get('stripe_card_token', None))
        return render_template('group_fitness.html', form=form, show_form=True,
                course=boot_camp, page_title="Group Fitness", card=card)

@app.route("/thank-you")
def thank_you():
    if 'registration_id' in session:
        registration = db_session.query(Registration).filter_by(
                id=session['registration_id']).one()
        card = find_card(registration.stripe_card_token)
        del session['registration_id']
        return render_template("thank_you.html", registration=registration,
                course=boot_camp, page_title="Thank You", card=card)
    else:
        return redirect("/group-fitness")

@app.route("/explode-all-pretty-like")
def explode_all_pretty_like():
    class TestError(RuntimeError):
        pass

    raise TestError("This error was triggered manually")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title="Not Found"), 404

@app.teardown_request
def shutdown_session(exception=None):
        db_session.remove()

@app.context_processor
def inject_stripe_public_key():
    return {'stripe_public_key': stripe_public_key}

@app.context_processor
def inject_google_analytics():
    return {'use_google_analytics': production_env}
