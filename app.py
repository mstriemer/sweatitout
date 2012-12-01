from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/instructors")
def instructors():
    return render_template("instructors.html")

@app.route("/group-fitness")
def group_fitness():
    return render_template("group_fitness.html")

@app.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")
