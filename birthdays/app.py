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
        month = request.form.get('month')
        day = request.form.get('day')

        if (not day in range(1, 32)) or (not month in range(1, 13)):

        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        # do i need to give an id to my inserted or is it given
        # i need to check whether the data fits what i want in my database
        # i need to make sure things are safe with server down???
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        # you should query into database
        # id INTEGER,
        # name TEXT,
        # month INTEGER,
        # day INTEGER,
        # PRIMARY KEY(id)
        #db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        # how do i extract data from sql
        # probably need to convert it to json

        db.execute("SELECT FROM birthdays *")
        #i want to create object in json format
        return render_template("index.html")


