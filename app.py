import sys
import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/login")
def login() :
    return render_template("login.html")

@app.route("/pleaseCheck")
def pleaseCheck() :
    return render_template("pleaseCheck.html")

@app.route("/registration")
def registration() :
    return render_template("registration.html")

@app.route("/version")
def version() :
    return render_template("version.html")

@app.route("/checkFix")
def checkFix() :
    return render_template("checkFix.html")

@app.route("/fix")
def fix() :
    return render_template("fix.html")

@app.route("/iframe")
def iframe() :
    return render_template("iframe.html")

@app.route("/write")
def write() :
    return render_template("write.html")

@app.route("/")
def index() :
    return "<script> location.href='/login'; </script>"


def main()  :
    app.debug = True
    app.run(host='0.0.0.0')

if __name__ == '__main__' :
    main()