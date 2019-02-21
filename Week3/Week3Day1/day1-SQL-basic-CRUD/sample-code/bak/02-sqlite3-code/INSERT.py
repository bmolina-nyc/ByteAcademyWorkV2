import csv
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "hurricanes.db"
CSVFILENAME = "hurricanes_fixed.csv"
DBPATH = os.path.join(DIRNAME, DBFILENAME)
CSVPATH = os.path.join(DIRNAME, CSVFILENAME)


def seed_from_csv(csvpath, dbpath):
    with open(csvpath, 'r') as csvfile, sqlite3.connect(dbpath) as connection:
        reader = csv.DictReader(csvfile)
        curs = connection.cursor()

        curs.execute("""DELETE FROM hurricanes;""")

        for dictline in reader:
            SQL = """INSERT INTO hurricanes(
                month,
                average,
                num2005,
                num2006,
                num2007,
                num2008,
                num2009,
                num2010,
                num2011,
                num2012,
                num2013,
                num2014,
                num2015) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            data = (dictline['month'], dictline['average'],
                    dictline['num2005'], dictline['num2006'],
                    dictline['num2007'], dictline['num2008'],
                    dictline['num2009'], dictline['num2010'],
                    dictline['num2011'], dictline['num2012'],
                    dictline['num2013'], dictline['num2014'],
                    dictline['num2015'])

            curs.execute(SQL, data)


if __name__ == "__main__":
    seed_from_csv(CSVPATH, DBPATH)
