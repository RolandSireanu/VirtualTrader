from . import app, db
from . import resources
from .Models import UserModel, Coins
from flask import redirect, render_template, request, url_for, session, make_response, jsonify, flash
from . import cryptoReader
from . import ProcesessRequest
import secrets
import ipdb



@app.route("/")
def main_route():
    return redirect("/login")



@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username");
        pswd = request.form.get("pswd");
        secondPswd = request.form.get("secondPswd");

        if(pswd != secondPswd):
            return render_template("register.html",valid="is-invalid", message="Passwords doesn't match !")
        
        userModel = UserModel.query.filter_by(username=username).first();
        if(userModel is None):
            ProcesessRequest.AddUserToDB(username=username, password=pswd);
            

            
            return redirect(url_for("login"));
        else:
            return render_template("register.html", valid="is-invalid", message="User already exists !")


    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if("user" in session):
        userModel = UserModel.query.filter_by(username=session.get("user")).first();
        prices = cryptoReader.readPrices()
        howMany = userModel.coinsOwned[0].getCoins()
        coins = [(p[0],p[1],howMany[p[0]]) for p in prices]
        return render_template("index.html", coins=coins, user=session["user"], money=round(userModel.money,2))
    else:
        return redirect(url_for("login"));

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "GET":
        return render_template("login.html",valid="")
    elif request.method == "POST":
        username = request.form.get("usr");
        password = request.form.get("pswd");

        if(username == "" or password == ""):
            flash("Fill in username and password !","danger")
        else:
            print(UserModel.query.all())
            usr = UserModel.query.filter_by(username=username).first()
            if usr is not None:
                if usr.password == password:
                    session["user"] = usr.username;
                    res = make_response(redirect(url_for("dashboard")))
                    token = secrets.token_hex(nbytes=4);
                    session["token"] = token;
                    res.set_cookie(key="token",value=token, expires="None",path="/", secure="False");
                    return res
                else:
                    flash("Invalid username or password", "danger")
            else:
                valid = False;
                flash("User doesn't exists in database","danger")
                 
        
        return render_template("login.html",valid="is-invalid");
    