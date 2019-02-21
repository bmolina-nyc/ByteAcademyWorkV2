import sqlite3
import os

PATH = os.path.dirname(__file__)
DBFILENAME = 'hurricanes_copy.db'
DBPATH = os.path.join(PATH, DBFILENAME)

def update():
    with sqlite3.connect(DBPATH) as connection:
        curs = connection.cursor()
        SQL = "UPDATE hurricanes SET num2005=?, num2006=? WHERE month=?";
        curs.execute(SQL, (100, 200, 'Nov'))
        curs.execute(SQL, (-5, -10, 'Dec'))

def insert():
    with sqlite3.connect(DBPATH) as connection:
        curs = connection.cursor()
        SQL = "INSERT INTO hurricanes(month, average, num2014, num2015) VALUES (?, ?, ?, ?)"
        # Lousy Smarch weather
        curs.execute(SQL, ('Smr', 10.0, 8, 12))
