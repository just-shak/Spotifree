#
#   definition of Bdd class
#
import sys
import mariadb


class Bdd:
    # initialisation de l'objet
    def __init__(self):
        self.name = "spotifree"
        self.connect = self.mariadb_connect()

    # destruction de l'objet
    def __del__(self):
        # fermeture de la connexion
        print("Connexion à spotifree fermée")
        self.connect.close()

    def mariadb_connect(self):
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

    def read_one(self, column_read="*", table_name="", column_match="", text=""):
        """read only first element that matches a texte
        @param column_read: name of column to fetch results, default value = "*"
        @param table_name: bdd table which is needed
        @param column_match: name of column where the match is needed, default value = ""
        @param text: string to be matched
        @return data : 1st line of bdd result as python tuple"""
        cursor = self.connect.cursor()

        if column_match != "":
            cursor.execute(
                f'select {column_read} from {table_name} where {column_match} like "{text}"'
            )
        else:
            cursor.execute(f'select {column_read} from {table_name}"')

        data = cursor.fetchone()
        if data is None:
            data = []
        return data

    def read_all(self, text, table_name, column_read="*", column_match=""):
        """read all elements found in bdd where a text is matched
        @param column_read: name of column to fetch results, default value = "*"
        @param table_name: bdd table which is needed
        @param column_match: name of column where the match is needed, default value = ""
        @param text: string to be matched
        @return data : 1st line of bdd result as python tuple"""
        cursor = self.connect.cursor()

        if column_match != "":
            cursor.execute(
                f'select {column_read} from {table_name} where {column_match} like "%{text}%"'
            )
        else:
            cursor.execute(f'select {column_read} from {table_name}"')

        data = list(cursor.fetchall())
        if data is None:
            data = []
        return data

    # generic write into mariadb
    def write(self, table_name, column, values):
        """sql request to write a new entry in spotifree bdd
        @param table_name: bdd table needed to insert new data
        @param column: name of columns to be filled (as python tuple)
        @param values: data to be inserted (as python tuple)
        """
        cursor = self.connect.cursor()

        request = f"insert into {table_name} ({', '.join(column)}) values ({', '.join('?' for _ in column)})"

        cursor.execute(request, values)
        self.connect.commit()
