import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)


def schema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS courses;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE courses(
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(64),
                    teachers_pk INTEGER,
                    FOREIGN KEY(teachers_pk) REFERENCES teachers(pk)
                    );"""
        cursor.execute(SQL)

        SQL = "DROP TABLE IF EXISTS teachers;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE teachers(
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(128)
                    );"""

        cursor.execute(SQL)

        SQL = """DROP TABLE IF EXISTS students;"""
        cursor.execute(SQL)

        SQL = """CREATE TABLE students(
                    pk INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(128)
                    );"""
        cursor.execute(SQL)

        SQL = """DROP TABLE IF EXISTS courses_students;"""

        cursor.execute(SQL)

        SQL = """CREATE TABLE courses_students(
                    courses_pk,
                    students_pk,
                    FOREIGN KEY(courses_pk) REFERENCES courses(pk),
                    FOREIGN KEY(students_pk) REFERENCES students(pk),
                    UNIQUE(courses_pk, students_pk)
                    );"""
        cursor.execute(SQL)


if __name__ == "__main__":
    schema(DBPATH)
