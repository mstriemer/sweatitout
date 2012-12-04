from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import stripe

from models import Registration, RegistrationForm

stripe.api_key = 'sk_test_q6yiThbRguk12pWKh0qlRsLn'

app = Flask(__name__)
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html")

@app.route("/group-fitness")
def group_fitness():
    form = RegistrationForm(course_slug='new-year-2013')
    return render_template("group_fitness.html", form=form)

@app.route("/new-year-2013/sign-up", methods=['POST'])
def sign_up():
    form = RegistrationForm(
            course_slug='new-year-2013',
            first_name=request.form.get('first_name', ''),
            last_name=request.form.get('last_name', ''),
            email=request.form.get('email', ''),
            phone=request.form.get('phone', ''))
    if form.valid():
        session = Session()
        return redirect("/thank-you")
    else:
        return render_template('group_fitness.html', form=form, show_form=True)

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

@app.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
