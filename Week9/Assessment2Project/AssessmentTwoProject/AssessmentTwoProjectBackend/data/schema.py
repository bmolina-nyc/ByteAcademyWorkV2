import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "bank.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename}"

        cur.execute(DROPSQL.format(tablename="branches"))

        SQL = """CREATE TABLE branches(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            branchName VARCHAR(128),
            city VARCHAR (128),
            state VARCHAR (32),
            zip INT NOT NULL
        );"""

        cur.execute(SQL)
    
        cur.execute(DROPSQL.format(tablename="employees"))
        
        SQL = """CREATE TABLE employees(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        branches_pk INT,
        fName VARCHAR(128),
        lName VARCHAR(128) NOT NULL,
        title VARCHAR(128),
        dob VARCHAR(128),
        FOREIGN KEY(branches_pk) REFERENCES branches(pk)
        );"""

        cur.execute(SQL)

if __name__=="__main__":
    schema(DBPATH)

