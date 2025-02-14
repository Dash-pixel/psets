import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name')
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))

        if ((not day in range(1, 32)) or (not month in range(1, 13))):
            return redirect('/')


        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?);", name, month, day)
        # i need to check whether the data fits what i want in my database
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthday_data = db.execute("SELECT * FROM birthdays")
        #should change to 1 argument
        return render_template("index.html", birthday_data=birthday_data)

