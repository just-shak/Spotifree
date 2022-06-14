import sys
from unicodedata import name
from users import Users
import mariadb


def mariadb_connect():
    """Connection to mariadb"""
    try:
        connected = mariadb.connect(
            user="spotuser",
            password="spotmdp",
            host="89.87.210.21",
            port=3306,
            database="spotifree",
        )
    except mariadb.Error as error:
        print(f"Error connecting to MariaDB Platform: {error}")
        sys.exit(1)
    return connected


def get_password(cursor, user: Users):
    cursor.execute(f'select * from users where name like "{user.name}"')
    for element in cursor:
        user.mdp = element[2]


def read(cursor, text, table_name, column):
    cursor.execute(f'select {column} from {table_name} where {column} like "{text}"')
    data = cursor.fetchone()
    if data is None:
        data = []
        return data
    else:
        return data


def main():

    # Initialisation de la connexion a mariadb
    bdd_connect = mariadb_connect()
    bdd_cursor = bdd_connect.cursor()

    # demande de connexion a l'utilisateur
    print("Bienvenue sur Spotifree!")
    print("Veuillez entrer l'identifiant:")
    spotifree_user = Users(input())

    # Verification de la présence de l'utilisateur
    if spotifree_user.name in read(bdd_cursor, spotifree_user.name, "users", "name"):
        print("Entrer le mot de passe:")
        mdp = input()
        get_password(bdd_cursor, spotifree_user)
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
            bdd_cursor.execute(
                "insert into users (name, mdp) values (?, ?)",
                (spotifree_user.name, spotifree_user.mdp),
            )
            bdd_connect.commit()
            print("Votre compte a bien été créé")
        else:
            print("A bientot sur spotifree !")

    # fermeture de la connection
    bdd_connect.close()
    print("Bbye")


if __name__ == "__main__":
    main()
