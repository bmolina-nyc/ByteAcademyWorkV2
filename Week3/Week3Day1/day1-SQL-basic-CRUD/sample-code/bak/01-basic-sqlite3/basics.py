import sqlite3
from pprint import pprint

connection = sqlite3.connect('school.db')
cursor = connection.cursor()

def quit():
    global connection
    connection.commit()
    connection.close()
    quit()

def SELECT():
    SQL = "SELECT * FROM courses;"
    cursor.execute(SQL)
    pprint(cursor.fetchall())

def SELECT_WHERE():
    SQL = "SELECT * FROM courses WHERE pk=1;"
    cursor.execute(SQL)
    print(cursor.fetchone())

def INSERT_INTO():
    SQL = "INSERT INTO courses(title, code, description) VALUES ('Theory of Computation', 'CS202', 'finite state machines, push down automata, and turing machines');"
    cursor.execute(SQL)

def UPDATE_WHERE():
    SQL = "UPDATE courses SET code='CS302' WHERE code='CS202';"
    cursor.execute(SQL)

def DELETE_WHERE():
    SQL = "DELETE FROM courses WHERE title='Theory of Computation';"
    cursor.execute(SQL)
