from RestApi import CryptoReader
from flask import Flask, render_template, redirect, request, url_for
from Validation import validate

c = CryptoReader();

app = Flask(__name__)

@app.route("/")
def main_route():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html",valid="")
    elif request.method == "POST":
        print("login POST")
        username = request.form.get("usr");
        password = request.form.get("pswd");
        print(username,password)
        if (validate(username, password) == False) :
            print("validation False");
            return render_template("login.html",valid="is-invalid", message="Wrong username & password !")
        else:
            return render_template("dashboard.html",coins=c.readPrices())

    else:
        return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")