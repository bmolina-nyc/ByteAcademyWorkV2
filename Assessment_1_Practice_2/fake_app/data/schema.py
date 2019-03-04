import os
import sqlite3

DIR = os.path.dirname(__file__)
DB = 'practice_db.db'
DBPATH = os.path.join(DIR, DB)

def schema(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cursor.execute(DROPSQL.format(tablename="tsla"))

        SQL = """CREATE TABLE tsla(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Open FLOAT,
                High FLOAT,
                Low FLOAT,
                Close FLOAT,
                AdjClose FLOAT,
                Volume FLOAT
            );"""
        cursor.execute(SQL)

        cursor.execute(DROPSQL.format(tablename="nhl"))

        SQL = """CREATE TABLE nhl(
                pk INTEGER PRIMARY KEY,
                Rk INTEGER,
                Player VARCHAR(128),
                Age INTEGER
            );"""
        cursor.execute(SQL)

if __name__ == "__main__":
    schema()