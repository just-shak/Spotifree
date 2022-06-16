from crypt import methods
import os
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()


@app.route("/")
def home():
    if "user" in session:
        return render_template("accueil.html", name=session["user"])
    return render_template("accueil.html")


@app.route("/login", methods=["POST"])
def login():
    session["user"] = request.form["user"]
    return redirect("/")


@app.route("/disconnect")
def disconnect():
    session.pop("user")
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
