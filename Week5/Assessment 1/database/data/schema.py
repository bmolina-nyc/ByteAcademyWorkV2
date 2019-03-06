import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'campus_students.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename}"

        cur.execute(DROPSQL.format(tablename="students"))

        SQL = """CREATE TABLE students(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            fname VARCHAR(128),
            lname VARCHAR(128),
            school VARCHAR(128),
            id VARCHAR(128),
            gpa FLOAT,
            campus_pk INTEGER, 
            FOREIGN KEY(campus_pk) REFERENCES campuses(pk)
        );"""
        cur.execute(SQL)


        cur.execute(DROPSQL.format(tablename="campuses"))

        SQL = """CREATE TABLE campuses(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(128),
            state VARCHAR(20)
        );"""
        cur.execute(SQL)

        
if __name__ == "__main__":
    schema()