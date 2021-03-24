from flask import render_template, request
from . import app

@app.errorhandler(404)
def handle404(e):

    print(e)
    return render_template("404.html")

@app.errorhandler(401)
def handle401(e):
    print(e)
    return render_template("401.html")

@app.errorhandler(500)
def handle500(e):
    print(e)
    return render_template("500.html")