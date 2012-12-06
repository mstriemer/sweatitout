from flask import Flask, render_template, request, redirect, session
from database import db_session
import stripe

from models import Course, Registration, RegistrationForm

stripe.api_key = 'sk_test_q6yiThbRguk12pWKh0qlRsLn'

app = Flask(__name__)
app.secret_key = 'a0s9fa09sfj01h389gef981g38fgq32f23f93'

boot_camp = Course(
        "new-year-2013",
        "New Year's Resolution Bootcamp",
        "Kickstart your new year's resolution with Sweat It Out Fitness's bootcamp. Perfect for all fitness levels this dynamic class offers cardio, resistence training, circuits and plyometrics and is different each and every time. Our small class sizes ensure lots of individual attention from Certified Personal Trainer Jenna Hobson and Personal Trainer Specialist Emily Striemer. Challenge yourself, get in shape and start 2013 off sweaty!",
        ["Mondays", "Thursdays"],
        "January 4th",
        "March 27th, 2013",
        "8:45",
        "9:45pm",
        "Revive Fitness Sage Creek")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html")

@app.route("/group-fitness")
def group_fitness():
    form = RegistrationForm(course_slug='new-year-2013')
    return render_template("group_fitness.html", form=form, course=boot_camp)

@app.route("/new-year-2013/register", methods=['POST'])
def sign_up():
    form = RegistrationForm(
            course_slug=boot_camp.slug,
            first_name=request.form.get('first_name', ''),
            last_name=request.form.get('last_name', ''),
            email=request.form.get('email', ''),
            phone=request.form.get('phone', ''))
    if form.valid():
        registration = form.build()
        db_session.add(registration)
        db_session.commit()
        session['registration_id'] = registration.id
        return redirect("/thank-you")
    else:
        return render_template('group_fitness.html', form=form, show_form=True,
                course=boot_camp)

@app.route("/thank-you")
def thank_you():
    if 'registration_id' in session:
        registration = db_session.query(Registration).filter_by(
                id=session['registration_id']).one()
        del session['registration_id']
        return render_template("thank_you.html", registration=registration,
                course=boot_camp)
    else:
        return redirect("/group-fitness")

@app.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.teardown_request
def shutdown_session(exception=None):
        db_session.remove()
