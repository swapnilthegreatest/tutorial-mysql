from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import Database.Celebs

class DatabaseCreator:
    def __init__(self, cnx, cursor):
        self.cnx = cnx
        self.cursor = cursor

    def create_database(self, db_name):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

        try:
            self.cursor.execute("USE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(db_name))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(self.cursor)
                print("Database {} created successfully.".format(db_name))
                self.cnx.database = db_name
            else:
                print(err)

    def create_tables(self, tables):
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def insert_rows(self, rows: dict):
        for table_name in rows.keys():
            print("Inserting data into {}".format(table_name))
            for query in rows[table_name]:
                try:
                    self.cursor.execute(query)
                    print("Query successful {}".format(query))
                except mysql.connector.Error as err:
                    print(err.msg)
            self.cnx.commit()
            print(self.cursor.rowcount, "record inserted.")

    def create_celeb_db(self):
        self.create_database(Database.Celebs.DB_NAME)
        self.create_tables(Database.Celebs.TABLES)
        self.insert_rows(Database.Celebs.ROWS)