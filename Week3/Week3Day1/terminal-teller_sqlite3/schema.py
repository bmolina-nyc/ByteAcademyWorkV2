import sqlite3

def create_table(dbname="backend_data.db"):
        with sqlite3.connect(dbname) as conn:
                cur = conn.cursor()
         
        SQL = """DROP TABLE IF EXISTS accounts; """
        cur.execute(SQL)

        SQL = """CREATE TABLE accounts (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                account_holder VARCHAR(128),
                account_number VARCHAR(128),
                pin VARCHAR(4),
                balance VARCHAR(128)
        );"""
        cur.execute(SQL)

if __name__ == "__main__":
    create_table()
