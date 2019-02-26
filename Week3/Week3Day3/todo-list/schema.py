import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "todo.db"
DBPATH = os.path.join(DIR, DBFILENAME)


def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"
        cur.execute(DROPSQL.format(tablename="users"))

        SQL = """CREATE TABLE users(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(16) NOT NULL,
            pin VARCHAR(4)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="todoitems"))

        SQL = """CREATE TABLE todoitems(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(256) NOT NULL,
            description TEXT,
            complete INTEGER DEFAULT 0,
            users_pk INTEGER,
            FOREIGN KEY (users_pk) REFERENCES users(pk)
            );"""

        cur.execute(SQL)


if __name__ == "__main__":
    schema()
