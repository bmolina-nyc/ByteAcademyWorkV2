import sqlite3
import csv


def create_tables():

    with open('employees.csv', 'r') as file:
        rows = []
        csv_file = csv.reader(file)
        next(csv_file, None) #skips header row
        for row in csv_file:
            if (len(row) == 6):
                rows.append(row)
            elif (len(row) == 7):
                row[5] = row[6] + row[5]
                del row[-1]
                rows.append(row)
       
    sql = sqlite3.connect('my_database.db')
    cur = sql.cursor()

    SQL = """DROP TABLE IF EXISTS employees; """
    cur.execute(SQL)

    SQL = """CREATE TABLE employees (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        person_name VARCHAR(128),
        cellphone VARCHAR(128),
        homephone VARCHAR(128),
        workphone VARCHAR(128),
        email VARCHAR(128),
        country VARCHAR(128)
    );"""
    cur.execute(SQL)

   

    SQL = "INSERT INTO employees (person_name, cellphone, homephone, workphone, email, country) VALUES (?, ?, ?, ?, ?, ?);"
    for row in rows:
        cur.execute(SQL, row)


    SQL = """DROP TABLE IF EXISTS phone_numbers; """
    cur.execute(SQL)

    SQL = """CREATE TABLE phone_numbers (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        cellphone VARCHAR(128),
        homephone VARCHAR(128),
        workphone VARCHAR(128)
    );"""
    cur.execute(SQL)

    SQL = "INSERT INTO phone_numbers(cellphone, homephone, workphone) VALUES (?,?,?);"
    for row in rows:
        cur.execute(SQL, (row[1], row[2], row[3]))
     
    sql.commit()

if __name__ == "__main__":
    create_tables()


# SELECT person_name, country
# FROM employees 
# WHERE country LIKE 'Gren%'

# SELECT *
# FROM employees 
# WHERE country LIKE 'Kore%'

# SELECT *
# FROM employees 
# WHERE person_name LIKE '%Cindy%'