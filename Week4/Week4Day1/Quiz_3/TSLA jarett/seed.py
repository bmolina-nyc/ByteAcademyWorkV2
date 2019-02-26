import csv
import os
import sqlite3
PATH = os.path.dirname(__file__)
INCSV = 'TSLA.csv'
CSV = os.path.join(PATH, INCSV)

def seed(dbname='TSLA.db'):

    with open(CSV, 'r') as in_file, sqlite3.connect(dbname) as conn:
        reader = csv.DictReader(in_file)
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM tsla""")

        for line in reader:
            SQL = """INSERT INTO tsla(
                Open,
                High,
                Low,
                Close,
                AdjClose,
                Volume) VALUES(?, ?, ?, ?, ?,?);"""

            data = (line['Open'], line['High'],
                    line['Low'], line['Close'],
                    line['Adj Close'], line['Volume'])
            cursor.execute(SQL, data)



if __name__ == "__main__":
    seed()