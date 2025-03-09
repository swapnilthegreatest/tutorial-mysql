import mysql
from mysql.connector.aio import MySQLConnectionAbstract
from mysql.connector.aio.abstracts import MySQLCursorAbstract

DB_NAME = 'celebs'

TABLES = dict()
TABLES['actors'] = (
    '''
        CREATE TABLE actors (
            actor_id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        ) ENGINE=InnoDB;
    ''')

TABLES['movies'] = (
    '''  
        CREATE TABLE movies (
            movie_id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            actor_id INT,
            movie_rating DOUBLE,
            FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
        ) ENGINE=InnoDB;
    '''
)

ROWS = dict()
ROWS['actors'] = [
    "INSERT INTO actors (actor_id, name) VALUES (1, 'John wick');",
    "INSERT INTO actors (actor_id, name) VALUES (2, 'Naruto');",
    "INSERT INTO actors (actor_id, name) VALUES (3, 'Sabrina');",
    "INSERT INTO actors (actor_id, name) VALUES (4, 'Mamta B.');",
]

ROWS['movies'] = [
    "INSERT INTO movies (movie_id, name, actor_id, movie_rating) VALUES (1, 'Parabellum', 1, 5.0);",
    "INSERT INTO movies (movie_id, name, actor_id, movie_rating) VALUES (2, 'Pain arc', 2, 5.0);",
    "INSERT INTO movies (movie_id, name, actor_id, movie_rating) VALUES (3, 'Chunin exams', 2, 4.0);",
    "INSERT INTO movies (movie_id, name, actor_id, movie_rating) VALUES (4, 'Capuchin', 3, 2.45);",
    "INSERT INTO movies (movie_id, name, actor_id, movie_rating) VALUES (5, 'Bengal', 4, 10.0);"
]

class CelebDB:
    def __init__(self, cnx: MySQLConnectionAbstract, cursor: MySQLCursorAbstract):
        self.db_name = 'celebs'
        self.cnx = cnx
        self.cursor = cursor

    def createActor(self, actor_id, name):
        query = "INSERT INTO actors (actor_id, name) VALUES ({0}, '{1}');".format(actor_id, name)
        try:
            self.cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print(err)

    def getActor(self, actor_id):
        query = "SELECT * FROM actors where actor_id = {0};".format(actor_id)
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except mysql.connector.Error as err:
            print(err)
