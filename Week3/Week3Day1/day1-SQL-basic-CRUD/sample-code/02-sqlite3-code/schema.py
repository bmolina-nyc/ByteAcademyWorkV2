import sqlite3
import os

BASEDIR = os.path.dirname(__file__)
DBFILENAME = "hurricanes.db"
DBPATH = os.path.join(BASEDIR, DBFILENAME)


def db_schema(database_path):
    with sqlite3.connect(database_path) as connection:
        curs = connection.cursor()
        curs.execute("""
            DROP TABLE IF EXISTS hurricanes;""")

        curs.execute("""
            CREATE TABLE hurricanes(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                month VARCHAR(3),
                average FLOAT,
                num2005 INTEGER,
                num2006 INTEGER,
                num2007 INTEGER,
                num2008 INTEGER,
                num2009 INTEGER,
                num2010 INTEGER,
                num2011 INTEGER,
                num2012 INTEGER,
                num2013 INTEGER,
                num2014 INTEGER,
                num2015 INTEGER
            );""")


if __name__ == "__main__":
    db_schema(DBPATH)
