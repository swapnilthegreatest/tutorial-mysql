import mysql.connector
from Database.DatabaseCreater import DatabaseCreator

#main file.
#play around with me in your brain cells.

if __name__ == '__main__':
    cnx = mysql.connector.connect(user='user', password='password')
    cursor = cnx.cursor()

    db_creator = DatabaseCreator(cnx, cursor)
    db_creator.create_celeb_db()

    cursor.close()
    cnx.close()
