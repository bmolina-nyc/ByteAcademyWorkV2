import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'books_words.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="books"))

        SQL = """CREATE TABLE books(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128),
            text_content TEXT,
            author VARCHAR(128)
        );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="words"))

        SQL = """CREATE TABLE words(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            books_pk INT,
            word INT,
            word_count INT,
            FOREIGN KEY(books_pk) REFERENCES books(pk)
        );"""

        cur.execute(SQL)

if __name__ == "__main__":
    schema()


# UNIQUE(accounts_pk, ticker)
