from users import Users
from bdd import Bdd
import pysftp


# def get_password(bdd: Bdd, user: Users):
#     data = bdd.read_one(user.name, "users", column_match="name")
#     # cursor.execute(f'select * from users where name like "{user.name}"')
#     user.mdp = data[2]


def connexion_user(bdd: Bdd):

    # # demande de connexion a l'utilisateur
    print("Bienvenue sur Spotifree!")
    print("Veuillez entrer un identifiant:")
    spotifree_user = Users(input())

    # bdd_cursor.execute("describe users")
    # for field in bdd_cursor.fetchall():
    #     print(field[0])

    # Verification de la présence de l'utilisateur
    if spotifree_user.name in bdd.read_one(
        column_read="name",
        table_name="users",
        column_match="name",
        text=spotifree_user.name,
    ):
        print("Entrer le mot de passe:")
        mdp = input()
        bdd.read_one(
            column_read="mdp",
            table_name="users",
            column_match="name",
            text=spotifree_user.name,
        )
        # get_password(bdd, spotifree_user)
        if mdp != spotifree_user.mdp:
            print("Mot de passe incorrect")
        else:
            print("Vous êtes connecté")

    # si l'utilisateur n'existe pas encore
    else:
        print("Identifiant inconnu")
        user_input = input("Voulez-vous créer un compte ? [o/n]")

        if user_input.lower() == "o" or user_input == "":
            print("Entrer le mot de passe:")
            spotifree_user.mdp = input()

            bdd.write(
                "users", ("name", "mdp"), (spotifree_user.name, spotifree_user.mdp)
            )
            print("Votre compte a bien été créé")
        else:
            print("A bientot sur spotifree !")

    print("Bbye")


def main():
    # Initialisation de la connexion a mariadb
    spotifree_bdd = Bdd()

    tmp = spotifree_bdd.read_all(
        table_name="music", column_match="artist", text="Chinese Man"
    )

    # connexion_user(spotifree_bdd)
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    print("Methode de connection au sftp de Félix")
    sftp = pysftp.Connection("90.89.5.238", username="fef", port=2121, cnopts=cnopts)

    # # Print de test
    # print(f"tmp: {tmp}")

    # # On affiche le resultat du read contenu dans la variable tmp
    print(f"rep musique: /{tmp[0][2]}/{tmp[0][3]}/{tmp[0][1]}")

    # # Méthode pour récupérer le track avec le bon chemin d'accès au sftp
    # sftp.get(f"/{tmp[0][2]}/{tmp[0][3]}/{tmp[0][1]}.mp3")
    sftp.close()


if __name__ == "__main__":
    main()
