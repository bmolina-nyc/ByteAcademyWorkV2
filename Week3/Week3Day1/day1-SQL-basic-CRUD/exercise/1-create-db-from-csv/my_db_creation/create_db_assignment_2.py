import sqlite3
import csv


def create_tables():
    db_filename = 'example2.db'

    with sqlite3.connect(db_filename) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * from example2')

        row = cur.fetchone()
        print(row.keys())



if __name__ == "__main__":
    create_tables()
