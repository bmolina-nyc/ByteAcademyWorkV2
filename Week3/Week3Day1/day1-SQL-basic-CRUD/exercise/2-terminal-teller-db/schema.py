import sqlite3

with sqlite3.connect('accounts.db') as conn:
    curs = conn.cursor()

    SQL = """ DROP TABLE IF EXISTS customers; """

    curs.execute(SQL)

    SQL = """ CREATE TABLE customers (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(128),
        account_number VARCHAR(16),
        pin VARCHAR(4),
        balance FLOAT); """
    
    curs.execute(SQL)
