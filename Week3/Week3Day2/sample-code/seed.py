import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath):
    courses = [
            ("Algebra", 1),         # pk 1
            ("English", 2),         # pk 2
            ("Social Studies", 2),  # pk 3
            ("Science", 3),         # pk 4
            ("P.E.", 1)]            # pk 5

    teachers = [
            ("Coach Gunn",), # pk 1,
            ("Dr. Weaver",), # pk 2,
            ("Mr. Hardister",)] # pk 3
    
    students = [
            ("Jamie",),  # pk 1,
            ("Charles",),    # pk 2,
            ("Martina",),    # pk 3,
            ("Mandissa",),   # pk 4,
            ("Logan",),      # pk 5,
            ("Robbie",)]     # pk 6
    
    courses_students = [
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 1),
            (3, 2),
            (3, 6),
            (4, 1),
            (4, 2),
            (4, 4),
            (4, 5)]

    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = """INSERT INTO courses(name, teachers_pk) VALUES (?, ?);"""
        for course in courses:
            curs.execute(SQL, course)

        SQL = """INSERT INTO teachers(name) VALUES (?);"""
        for teacher in teachers:
            curs.execute(SQL, teacher)

        SQL = """INSERT INTO students(name) VALUES (?);"""
        for student in students:
            curs.execute(SQL, student)

        SQL = """INSERT INTO courses_students VALUES (?, ?);"""
        for course_student in courses_students:
            curs.execute(SQL, course_student)

if __name__ == "__main__":
    seed(DBPATH)
