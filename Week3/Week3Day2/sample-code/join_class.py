import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def join_class(studentname, coursename, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()

        SQL = "SELECT pk FROM students WHERE name = ?;"
        curs.execute(SQL, (studentname,))
        result = curs.fetchone()
        if not result:
            raise ValueError
        students_pk = result[0]

        SQL = "SELECT pk FROM courses WHERE name = ?;"
        curs.execute(SQL, (coursename,))
        result = curs.fetchone()
        if not result:
            raise ValueError
        courses_pk = result[0]

        SQL = """INSERT INTO courses_students(courses_pk, students_pk)
                    VALUES(?, ?);"""
        curs.execute(SQL, (courses_pk, students_pk))
