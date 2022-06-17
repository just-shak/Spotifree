import os

# import pour modules applicatifs python sur une page web (installer flask avec pip install)
from flask import Flask, render_template, request, redirect, session

# imports pour les Forms (installer flask_wtf avec pip install)
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
from bdd import Bdd

# class pour utiliser les forms dans /profile
# class MyForm(FlaskForm):
#    name = StringField("name", validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = os.urandom(12).hex()
spotifree_bdd = Bdd()
# form = MyForm()
data = []
err = False
msg = ""


# Test session d'utilisateur sur la racine
@app.route("/")
def home():
    if "user" in session:
        return render_template("accueil.html", datas=data, name=session["user"])

    return render_template("accueil.html")


# Lors de la connexion on se logue
@app.route("/login", methods=["POST"])
def login():
    session["email"] = request.form["email"]
    # TODO verification des champs remplis
    # match de l'email dans la BDD user
    if request.form["email"] in spotifree_bdd.read_one(
        column_read="email",
        table_name="users",
        column_match="email",
        text=request.form["email"],
    ):
        # redirection a la page de base TODO: redirection sur /profil
        return redirect("/music_search")
    else:
        # Erreur d'identifiants
        msg = "Identifiants Inconnus"
        return redirect("/register")


# Pour de déconnecter de la session TODO ajout bouton deconnection
@app.route("/disconnect")
def disconnect():
    session.pop("user")
    data.clear()
    return redirect("/")


# Formulaire d'inscription à spotifree
@app.route("/register_form", methods=["POST"])
def register_form():
    # match des mots de passe entrés par l'utilisateur
    if request.form["password"] == request.form["password2"]:
        # sauvegarde de l'utilisateur dans la bdd
        spotifree_bdd.write(
            "users",
            ("name", "mdp", "email"),
            (request.form["user"], request.form["password"], request.form["email"]),
        )
        # redirection a la page principale
        return redirect("/music_search")
    else:
        # sinon indication d'une erreur dans le mot de passe TODO mdp faible/fort
        err = True
        return render_template("register2.html", err=err)


# redirection a register form lor d'un post TODO: changer et ajouter methode 'GET' à register_form
@app.route("/register")
def register():
    return render_template("register2.html")


# page de recherche de musique, exemple de résultat avec le mot clef "Chinese"
@app.route("/music_search", methods=["GET", "POST"])
def music_search():
    # Si bouton submit est utilisé et qu'il y a des infos reçues
    if request.method == "POST" and request.form["music_keyword"] != "":
        # récupère dans la bdd les matchs de recherche selont les titres, artistes, albums
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
        # Si un resultat est présent on renvoie les donées a la page web search.html
        if tracks or albums or artists:
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
    # methodes pour tester le retour d'information sur la page TODO: a supprimer
    if request.method == "GET":
        return render_template(
            "search.html", msg="get", results=False, request=request.method
        )
    if request.method == "POST" and request.form["music_keyword"] == "":
        return render_template(
            "search.html", msg="post", results=False, request=request.method
        )
    # retour par defaut de la page web TODO remove les données a afficher sur la page web qui servent aux tests
    return render_template(
        "search.html", msg="pas de if", results=False, request=request.method
    )


# page playlist TODO
@app.route("/playlists")
def playlists():
    return render_template("playlists.html")


# Page sociale des amis TODO
@app.route("/spotifriends")
def spotifriends():
    return render_template("social_list.html")


# TODO a tester pour ajouter des boutons de connexion
# @app.route("/profile", methods=["GET", "POST"])
# def profile():
#     if form.validate_on_submit():
#         if "music" in request.form:
#             return redirect("/music_search")
#         elif "playlist" in request.form:
#             return redirect("/playlist")
#         elif "spotifriends" in request.form:
#             return redirect("/spotifriends")

#     return render_template("profile.html")


if __name__ == "__main__":
    app.run()
