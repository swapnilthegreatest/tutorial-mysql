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