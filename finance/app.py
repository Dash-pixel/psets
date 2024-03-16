import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stock_list = db.execute('SELECT symbol, quantity FROM bought WHERE user_id = ?', session.get('user_id'))
    for i in stock_list:
        i['current_price'] = lookup(i['symbol'])
        i['current_price']= i['current_price'] * int(i['quantity'])

    return render_template('index.html', stock_rows = stock_list)
    #return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'GET':
        return render_template("buy.html")

    else:
        symbol = (request.form.get("symbol")).upper()
        quantity = int(request.form.get("quantity"))

        stock_info = lookup(symbol)
        if stock_info == None:
            return apology("No such stock")

        if quantity <= 0:
            return apology("do not play tricks, u r a fkng looser and will never become a hacker")


        to_pay = stock_info['price'] * quantity

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get('user_id'))[0]['cash'] #what?

        if to_pay > cash:
            return apology("NO MONEY")

        new_cash = cash - to_pay
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session.get('user_id'))

        affected_rows = db.execute("UPDATE bought SET quantity = quantity + ? WHERE user_id = ? AND symbol = ?", quantity, session.get('user_id'), symbol)
        if affected_rows == 0:
            db.execute("INSERT INTO bought (user_id, symbol, quantity) VALUES (?, ?, ?)", session.get('user_id'), symbol, quantity)

        return redirect('/')

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'GET':
        return render_template("quote.html")

    else:
        symbol = request.form.get("symbol")
        stock_info = lookup(symbol)

        if stock_info == None:
            return apology("stock doesnt exist")

        return render_template('quoted.html', stock_info = stock_info)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if ((confirmation != password) or (username == '') or (password == '')):
            return apology("something with the detailes")

        exists = db.execute('SELECT username FROM users WHERE username == ? LIMIT 1', username)

        if exists:
            return apology("the username's taken")

        hash = generate_password_hash(password)

        db.execute('INSERT INTO users (username, hash) VALUES(?, ?)', username, hash)
        user_id = db.execute('SELECT id FROM users WHERE username == ?', username)

        session['user_id'] = user_id[0]['id']

        return redirect('/')

    else:
        return render_template("registration.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == 'GET':
        return render_template('sell.html')
    else:
        symbol = request.form.get("symbol")
        quantity = request.form.get("quantity")
        return apology("TODO")
