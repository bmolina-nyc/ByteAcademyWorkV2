# getting the pk from the most recent INSERT
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRNAME, DBFILENAME)


def create_student(studentname, dbpath=DBPATH):
    # INSERT a new student, return the new pk
    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = "INSERT INTO students(name) VALUES(?);"
        curs.execute(SQL, (studentname, ))
        pk = curs.lastrowid  # cursor.lastrowid = new pk of last INSERT
        return pk
