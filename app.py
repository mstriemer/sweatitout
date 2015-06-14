import os
import smtplib
import threading
from collections import OrderedDict
from datetime import datetime
from email.mime.text import MIMEText
from functools import wraps

from flask import (Flask, jsonify, render_template, request, redirect, session,
                   abort)

from database import db_session

from models import ProgramDesignRegistration, Registration, RegistrationForm
from courses import (active_courses, all_courses, upcoming_courses)

from auth import login_required

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# From https://github.com/kennethreitz/flask-sslify/blob/master/flask_sslify.py
def https_required(f):
    """Redirect incoming requests to HTTPS."""
    @wraps(f)
    def decorated(*args, **kwargs):
        criteria = [
            request.is_secure,
            app.debug,
            request.headers.get('X-Forwarded-Proto', 'http') == 'https'
        ]

        if not any(criteria):
            if request.url.startswith('http://'):
                url = request.url.replace('http://', 'https://', 1)
                return redirect(url, code=302)
        return f(*args, **kwargs)
    return decorated

smtp_host, smtp_port = 'smtp.gmail.com', 587
sender = 'admin@sweatitoutfit.com'
sender_password = os.environ.get('ERROR_SMTP_PASSWORD')
production_env = os.environ.get('APP_ENV', None) == 'production'

if production_env:
    app.secret_key = os.environ['FLASK_SECRET_KEY']
    if not sender_password:
        raise RuntimeError('ERROR_SMTP_PASSWORD required')
    ADMINS = ['mstriemer@gmail.com']
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(
        (smtp_host, smtp_port),
        sender,
        ADMINS,
        '[Sweat It Out][Error] An Error Occurred',
        (sender, sender_password),
        ()
    )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
else:
    app.secret_key = 'a0s9fa09sfj01h389gef981g38fgq32f23f93'


def send_mail(recipients, subject, text):
    if not production_env:
        # Skip sending mail in development.
        return
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    server = smtplib.SMTP('{smtp_host}:{smtp_port}'.format(
        smtp_host=smtp_host, smtp_port=smtp_port))
    server.starttls()
    server.login(sender, sender_password)
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/instructors")
def instructors():
    return render_template("instructors.html", page_title="Instructors")


def render_group_fitness(active_course=None, active_form=None):
    def make_form(course):
        if course == active_course:
            form = active_form
        else:
            form = RegistrationForm(course_slug=course.slug, instance=course)
        return (course, form)

    def make_forms(all_courses):
        return [make_form(course) for course in all_courses]

    return render_template("group_fitness.html",
                           upcoming_courses=make_forms(upcoming_courses),
                           active_courses=make_forms(active_courses),
                           page_title="Group Fitness")


@app.route("/program-design", methods=["POST"])
def program_design_signup():
    if not request.json:
        response = jsonify(**{'errors': {'request': ['is not valid JSON']}})
        response.status_code = 400
        return response
    fields = ['name', 'email', 'trainer', 'package']
    values = {}
    errors = {}
    for field in fields:
        values[field] = request.json.get(field)
        if not values[field]:
            errors[field] = ['is required']
        elif len(values[field]) > 255:
            errors[field] = ['must be less than 255 characters long']
    if errors:
        response = jsonify(**{'errors': errors})
        response.status_code = 422
        return response
    else:
        registration = ProgramDesignRegistration(**values)
        registration.registration_date = datetime.now()
        db_session.add(registration)
        db_session.commit()
        # Send an email later.
        threading.Thread(
            target=send_mail,
            args=(
                ADMINS + [registration.trainer_email],
                '[Sweat It Out] New program design registration',
                registration_email_text(registration),
            ),
        ).start()
        json_data = {field: getattr(registration, field)
                     for field in fields + ['id', 'registration_date']}
        response = jsonify(**json_data)
        response.status_code = 201
        return response


def registration_email_text(registration):
    registration_data = OrderedDict([
        ('name', registration.name),
        ('email', registration.email),
        ('trainer', registration.trainer),
        ('package', registration.package),
        ('registration_date', registration.registration_date.strftime('%c')),
    ])
    return '\n'.join('{k}: {v}'.format(k=k, v=v)
                     for k, v in registration_data.items())


def send_registration_email(pk):
    registration = db_session.query(ProgramDesignRegistration).get(pk)
    to = ADMINS + [registration.trainer_email]
    message = registration_email_text(registration)
    send_mail(to, '[Sweat It Out] New program design registration', message)


@app.route("/program-design")
def program_design():
    return render_template("program_design.html", page_title="Program Design")


@app.route("/group-fitness")
def group_fitness():
    return render_group_fitness()


@app.route("/group-fitness/<slug>/register")
def redirect_to_group_fitness(slug):
    return redirect("/group-fitness")


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
        referrer_name=request.form.get('referrer_name', ''),
        assessments=request.form.get('assessments', ''),
        instance=course,
    )
    if form.valid():
        registration = form.build()
        db_session.add(registration)
        db_session.commit()
        session['registration_id'] = registration.id
        return redirect("/thank-you")
    else:
        form.active = True
        return render_group_fitness(course, form)


@app.route("/thank-you")
def thank_you():
    if 'registration_id' in session:
        registration = db_session.query(Registration).filter_by(
            id=session['registration_id']).one()
        course = find_course(registration.course_slug)
        del session['registration_id']
        return render_template("thank_you.html", registration=registration,
                               course=course, page_title="Thank You")
    else:
        return redirect("/group-fitness")


@app.route("/registrations")
@https_required
@login_required
def registrations():
    registrations = db_session.query(Registration)
    registrations = registrations.order_by('registration_date DESC').all()
    return render_template("registrations.html", registrations=registrations)


@app.route("/explode-all-pretty-like")
def explode_all_pretty_like():
    raise TestError("This error was triggered manually")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title="Hmmmmm"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', page_title="Uh oh"), 500


@app.teardown_request
def shutdown_session(exception=None):
        db_session.remove()


@app.context_processor
def inject_globals():
    return {
        'sections': [
            ["/", "Home"],
            ["/group-fitness", "Group Fitness"],
            ["/program-design", "Program Design"],
            ["/instructors", "Instructors"],
        ],
        'use_google_analytics': production_env,
        'debug': app.debug,
    }


@app.template_filter('currency')
def currency_filter(currency):
    return '${:.2f} CAD'.format(currency)


def find_course(slug):
    for c in all_courses:
        if c.slug == slug:
            return c
    raise ValueError('could not find course {}'.format(slug))


class TestError(RuntimeError):
    pass
