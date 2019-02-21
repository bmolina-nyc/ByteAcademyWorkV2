## examples of JOIN selections
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "school.db"
DBPATH = os.path.join(DIRNAME, DBFILENAME)

def student_from_pk(pk, dbpath=DBPATH):
    pass

def teacher_for_course(coursename, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        # this is a "magic" line of code that has .fetchone() and .fetchall()
        # return dictionary-like objects with column names for keys
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        SQL = """ SELECT teachers.name 
                  FROM teachers JOIN courses
                  ON teachers.pk = courses.teachers_pk
                  WHERE courses.name = ?; """
        curs.execute(SQL, (coursename,))
        result = curs.fetchone()
        if not result:
            return None
        else:
            return result['name']

def courses_for_teacher(teachername):
    pass

def students_for_course(coursename, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        # this is a "magic" line of code that has .fetchone() and .fetchall()
        # return dictionary-like objects with column names for keys
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        SQL = """ SELECT students.name 
                  FROM courses JOIN courses_students
                    ON courses.pk = courses_students.courses_pk
                               JOIN students
                    ON students.pk = courses_students.students_pk
                  WHERE courses.name = ?; """
        curs.execute(SQL, (coursename,))
        results = curs.fetchall()

        return [result['name'] for result in results]

# join on four tables!
def students_for_teacher(teachername, dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        SQL = """ SELECT students.name 
                    FROM teachers JOIN courses 
                        ON teachers.pk = courses.teachers_pk 
                                  JOIN courses_students 
                        ON courses.pk = courses_students.courses_pk 
                                  JOIN students 
                        ON students.pk = courses_students.students_pk 
                    WHERE teachers.name = ?; """
        curs.execute(SQL, (teachername,))
        results = curs.fetchall()

        return [result['name'] for result in results]
