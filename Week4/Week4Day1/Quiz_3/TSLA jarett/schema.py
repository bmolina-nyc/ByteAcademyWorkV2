import os
import sqlite3

DIR = os.path.dirname(__file__)
DB = 'TSLA.db'
DBPATH = os.path.join(DIR, DB)


# Open,High,Low,Close,Adj Close,Volume

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS tsla")
        
        SQL =  """CREATE TABLE tsla(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                Open FLOAT,
                High FLOAT,
                Low FLOAT,
                Close FLOAT,
                AdjClose FLOAT,
                Volume FLOAT
            );"""
        cursor.execute(SQL)


if __name__ == "__main__":
    schema()