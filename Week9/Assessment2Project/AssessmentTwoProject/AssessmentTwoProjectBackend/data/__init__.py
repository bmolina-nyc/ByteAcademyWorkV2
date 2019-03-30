import sqlite3
import os 

DIR = os.path.dirname(__file__)
DBFILENAME = "bank.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"
        cur.execute(DROPSQL.format(tablename="accounts"))
