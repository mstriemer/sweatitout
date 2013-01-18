import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, session, abort
from database import db_session

from models import Course, Registration, RegistrationCharge, RegistrationForm

app = Flask(__name__)

production_env = os.environ.get('APP_ENV', None) == 'production'
if production_env:
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
    app.secret_key = 'a0s9fa09sfj01h389gef981g38fgq32f23f93'

boot_camp = Course(
        "new-year-2013",
        "New Year's Resolution Bootcamp",
        "Kickstart your new year's resolution with Sweat It Out Fitness's bootcamp. Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
        ["Mondays", "Thursdays"],
        "January 7th",
        "February 14th, 2013",
        "8:45",
        "9:45pm",
        "Revive Fitness Sage Creek",
        110,
        None,
        False,
        "/static/images/revive-fitness-sage-creek.png",
        "https://maps.google.ca/maps?q=Revive+Fitness+Sage+Creek&hl=en&ll=49.833886,-97.049017&spn=0.019432,0.045447&sll=49.83444,-97.1521&sspn=0.621812,1.454315&hq=Revive+Fitness+Sage+Creek&t=m&z=15&iwloc=A",
        )
winter = Course(
        "second-chance-bootcamp-2013",
        "Second Chance New Year's Resolution Bootcamp",
        "Didn't start on Janurary 1st? Don't worry about it, start February 5th instead! Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson. Make 2013 your best year!",
        ["Tuesdays", "Thursdays"],
        "February 5th",
        "March 14th, 2013",
        "7:00",
        "8:00pm",
        "Revive Fitness Polo Park",
        110,
        60,
        True,
        "/static/images/revive-fitness-polo-park.png",
        "https://maps.google.ca/maps?q=1740+Ellice+Avenue+(Revive+Fitness+Polo+Park)&hl=en&sll=49.864325,-97.124977&sspn=0.155357,0.363579&hnear=1740+Ellice+Ave,+Winnipeg,+Manitoba+R3H+0B6&t=m&z=16&iwloc=A",
        )

courses = [winter, boot_camp]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html", page_title="Instructors")

@app.route("/group-fitness")
def group_fitness():
    course = winter
    form = RegistrationForm(course_slug=course.slug)
    old_courses = [c for c in courses if c != course]
    return render_template("group_fitness.html", form=form, course=course,
            old_courses=old_courses, page_title="Group Fitness")

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
            attendance=request.form['attendance'],
    )
    if form.valid():
        registration = form.build()
        db_session.add(registration)
        db_session.commit()
        session['registration_id'] = registration.id
        return redirect("/thank-you")
    else:
        return render_template('group_fitness.html', form=form, show_form=True,
                course=course, page_title="Group Fitness")

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
def inject_google_analytics():
    return {'use_google_analytics': production_env}

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
