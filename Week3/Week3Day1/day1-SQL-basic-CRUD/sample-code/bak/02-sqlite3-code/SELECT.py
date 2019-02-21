import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILE = 'hurricanes.db'


def fill_vals(row):
    keys = ("month", "average", "num2005", "num2006", "num2007", "num2008",
            "num2009", "num2010", "num2011", "num2012", "num2013", "num2014",
            "num2015", "COUNT(*)")
    dictionary = dict(row)
    defaults = {}
    for key in keys:
        defaults[key] = dictionary.get(key)
    return defaults


def print_row(row):
    outputfmt = """month {month}, average {average},
2005: {num2005}, 2006: {num2006}, 2007: {num2007},
2008: {num2008}, 2009: {num2009}, 2010: {num2010},
2011: {num2011}, 2012: {num2012}, 2013: {num2013},
2014: {num2014}, 2015: {num2015}, COUNT(*): {COUNT(*)}

"""
    print(outputfmt.format(**fill_vals(row)))


def fetch_one(SQL, vals=tuple()):
    print(SQL, vals, sep='\n')
    with sqlite3.connect(DBFILE) as connection:
        connection.row_factory = sqlite3.Row  # return rows with keys
        curs = connection.cursor()
        curs.execute(SQL, vals)
        row = curs.fetchone()
        if not row:
            print("Nothing returned")
            return
        print_row(row)


def fetch_all(SQL, vals=tuple()):
    print(SQL, vals, sep='\n')
    with sqlite3.connect(DBFILE) as connection:
        connection.row_factory = sqlite3.Row  # return rows with keys
        curs = connection.cursor()
        curs.execute(SQL, vals)
        rows = curs.fetchall()
        if not rows:
            print("Nothing returned")
        for row in rows:
            print_row(row)


def select_count():
    SQL = "SELECT COUNT(*) FROM hurricanes;"
    fetch_one(SQL)


def select_equal():
    SQL = "SELECT * FROM hurricanes WHERE num2007=?;"
    fetch_all(SQL, (1, ))


def select_limit():
    SQL = "SELECT * FROM hurricanes LIMIT 3;"


def select_columns():
    SQL = "SELECT month, average FROM hurricanes WHERE average > ? ORDER BY average ASC;"
    fetch_all(SQL, (1.0, ))
