import os
from flask import Flask, render_template, request, redirect, session
from bdd import Bdd

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()
spotifree_bdd = Bdd()
data = []


@app.route("/")
def home():
    if "user" in session:
        return render_template("accueil.html", datas=data, name=session["user"])

    return render_template("accueil.html")


@app.route("/login", methods=["POST"])
def login():
    session["email"] = request.form["email"]
    if request.form["email"] in spotifree_bdd.read_one(
        column_read="email",
        table_name="users",
        column_match="email",
        text=request.form["email"],
    ):
        # data.append(request.form["email"])
        return redirect("/music_search")
    else:
        return redirect("/register")


# @app.route("/login", methods=["POST"])
# def login():
#     session["user"] = request.form["user"]
#     data.append(request.form["user"])
#     # if request.form["email"] in spotifree_bdd.read_one(
#     #     column_read="email",
#     #     table_name="users",
#     #     column_match="email",
#     #     text=request.form["email"],
#     # ):
#     #     return redirect("/music_search")
#     # else:
#     #     return redirect("/register2")
#     return redirect("/")


@app.route("/disconnect")
def disconnect():
    session.pop("user")
    data.clear()
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register2.html")


@app.route("/music_search")
def music_search():
    return render_template("search.html")


@app.route("/playlists")
def playlists():
    return render_template("playlists.html")


@app.route("/spotifriends")
def spotifriends():
    return render_template("social_list.html")


if __name__ == "__main__":
    app.run()
