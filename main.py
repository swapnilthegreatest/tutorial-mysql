import mysql.connector

from Database.Celebs import CelebDB
from Database.DatabaseCreater import DatabaseCreator

#main file.
#play around with me in your brain cells.

if __name__ == '__main__':
    cnx = mysql.connector.connect(user='user', password='password')
    cursor = cnx.cursor()

    db_creator = DatabaseCreator(cnx, cursor)
    db_creator.create_celeb_db()

    celeb_db = CelebDB(cnx, cursor)
    celeb_db.createActor(6, 'Bajirao')
    data = celeb_db.getActor(6)
    print(data)

    cursor.close()
    cnx.close()
