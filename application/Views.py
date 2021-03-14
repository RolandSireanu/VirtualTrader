from . import app, db
from . import resources
from .Models import UserModel
from flask import redirect, render_template, request, url_for, session
from . import cryptoReader
import ipdb



@app.route("/")
def main_route():
    return redirect("/login")

@app.route("/dashboard")
def dashboard():
    if("user" in session):
        return render_template("dashboard.html", coins=cryptoReader.readPrices())
    else:
        return redirect(url_for("login"));

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html",valid="")
    elif request.method == "POST":
        valid = True;
        msg = "";
        username = request.form.get("usr");
        password = request.form.get("pswd");
        
        if(username == "" or password == ""):
            valid = False;
            msg = "Fill in username and password !";
        else:
            usr = UserModel.query.filter_by(username=username).first()
            if usr is not None:
                if usr.password == password:
                    session.permanent = True;
                    session["user"] = usr.username;
                    return redirect(url_for("dashboard"))
                else:
                    valid = False;
                    msg = "Invalid username or password";
            else:
                valid = False;
                msg = "Invalid username or password";            
        
        return render_template("login.html",valid="is-invalid",message=msg);
    