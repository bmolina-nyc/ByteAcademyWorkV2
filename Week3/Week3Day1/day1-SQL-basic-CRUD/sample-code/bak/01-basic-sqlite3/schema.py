import sqlite3


def create_table(dbname="school.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()
        SQL = """DROP TABLE IF EXISTS courses; """

        cur.execute(SQL)

        SQL = """CREATE TABLE courses (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128),
            code VARCHAR(6),
            description TEXT
        );"""

        cur.execute(SQL)


if __name__ == "__main__":
    create_table()
