import csv
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "tsla.db"
CSVFILENAME = "TSLA.csv"
DBPATH = os.path.join(DIRNAME, DBFILENAME)
CSVPATH = os.path.join(DIRNAME, CSVFILENAME)

def seed_from_csv(csvpath, dbpath):
    with open(csvpath, 'r') as csvfile, sqlite3.connect(dbpath) as connection:
        reader = csv.DictReader(csvfile)
        curs = connection.cursor()

        curs.execute("""DELETE FROM tsla;""")

        for dictline in reader:
            SQL = """INSERT INTO tsla(
                Open,
                High,
                Low,
                Close,
                Adj_Close,
                Volume) VALUES(?, ?, ?, ?, ?, ?);"""

            data = (dictline['Open'], dictline['High'], dictline['Low'], dictline['Close'], dictline['Adj Close'], dictline['Volume'])

            curs.execute(SQL, data)


if __name__=="__main__":
    seed_from_csv(CSVPATH, DBPATH)



























