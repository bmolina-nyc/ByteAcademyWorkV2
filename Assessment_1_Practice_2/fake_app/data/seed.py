import csv
import os
import sqlite3

PATH = os.path.dirname(__file__) # the path from the python exec to that file
NHLCSV = 'NHL_2018.csv'
TSLACSV = 'TSLA.csv'
NHLPATH = os.path.join(PATH, NHLCSV)
TSLAPATH = os.path.join(PATH, TSLACSV)

DB = 'practice_db.db'
DBPATH = os.path.join(PATH, DB)

def seed(dbname=DBPATH):
    #TSLA
    with open(TSLAPATH, 'r') as file, sqlite3.connect(dbname) as conn:
        reader = csv.DictReader(file)
        cursor = conn.cursor()
     
        cursor.execute("""DELETE FROM tsla""")

        for line in reader:
            SQL = """INSERT INTO tsla(
                Open,
                High,
                Low,
                Close,
                AdjClose,
                Volume) 
                VALUES(?,?,?,?,?,?);"""

            data = (line['Open'], line['High'], 
                line['Low'], line['Close'], 
                line['AdjClose'], line['Volume'])

            cursor.execute(SQL, data)


    #nhl
    with open(NHLPATH, 'r') as file, sqlite3.connect(dbname) as conn:
        nhlreader = csv.DictReader(file)
        cursor = conn.cursor()
      
        cursor.execute("""DELETE FROM nhl""")

        for line in nhlreader:
            SQL = """INSERT INTO nhl(
                Rk,
                Player,
                Age
               )
                VALUES(?,?,?);"""
            
            nhldata = (line['Rk'], line['Player'], line['Age'])

            cursor.execute(SQL, nhldata)


if __name__ == "__main__":
    seed()