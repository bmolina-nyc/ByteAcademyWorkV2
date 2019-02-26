import csv
import os
import sqlite3

BASEDIR = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
DBPATH = os.path.join(BASEDIR, DBFILENAME)


def db_schema(database_path):
    with sqlite3.connect(database_path) as connection:
        curs = connection.cursor()
        curs.execute("""DROP TABLE if EXISTS tsla;""")

        curs.execute("""
            CREATE TABLE tsla(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Open FLOAT,
                High FLOAT,
                Low FLOAT,
                Close FLOAT,
                Adj_Close FLOAT,
                Volume FLOAT
            );""")

if __name__=="__main__":
    db_schema(DBPATH)





















