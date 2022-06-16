from cgitb import reset
from mailbox import MaildirMessage
from mmap import MAP_PRIVATE
import os
from re import A
from unittest import result
from flask import Flask, render_template, request, redirect, session
from bdd import Bdd

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()
spotifree_bdd = Bdd()
data = []
err = False
msg = ""


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
        return redirect("/music_search")
    else:
        msg = "Identifiants Inconnus"
        return redirect("/register")


@app.route("/disconnect")
def disconnect():
    session.pop("user")
    data.clear()
    return redirect("/")


@app.route("/register_form", methods=["POST"])
def register_form():
    if request.form["password"] == request.form["password2"]:
        spotifree_bdd.write(
            "users",
            ("name", "mdp", "email"),
            (request.form["user"], request.form["password"], request.form["email"]),
        )
        return redirect("/music_search")
    else:
        err = True
        return render_template("register2.html", err=err)


@app.route("/register")
def register():
    return render_template("register2.html")


@app.route("/music_search", methods=["GET", "POST"])
def music_search():
    if request.method == "POST" and request.form["music_keyword"] != "":
        tracks = spotifree_bdd.read_all(
            table_name="music", column_match="title", text=request.form["music_keyword"]
        )
        artists = spotifree_bdd.read_all(
            table_name="music",
            column_match="artist",
            text=request.form["music_keyword"],
        )
        albums = spotifree_bdd.read_all(
            table_name="music",
            column_match="album",
            text=f'{request.form["music_keyword"]}',
        )
        # tracks = ["Hola", "Coucou", "Salut", "Bonjour"]
        if tracks or albums or artists:  # or artists or album:
            return render_template(
                "search.html",
                msg="Resultats:",
                results=True,
                tracks=tracks,
                albums=albums,
                artists=artists,
            )
        else:
            return render_template(
                "search.html", results=True, msg="Aucun resultat trouvé"
            )
    if request.method == "GET":
        return render_template(
            "search.html", msg="get", results=False, request=request.method
        )
    if request.method == "POST" and request.form["music_keyword"] == "":
        return render_template(
            "search.html", msg="post", results=False, request=request.method
        )
    return render_template(
        "search.html", msg="pas de if", results=False, request=request.method
    )


@app.route("/playlists")
def playlists():
    return render_template("playlists.html")


@app.route("/spotifriends")
def spotifriends():
    return render_template("social_list.html")


if __name__ == "__main__":
    app.run()
