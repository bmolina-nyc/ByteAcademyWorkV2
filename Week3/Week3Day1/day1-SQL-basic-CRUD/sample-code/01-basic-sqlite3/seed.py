import sqlite3

def seed(dbname="school.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        SQL = """DELETE FROM courses;"""
        cur.execute(SQL)

        SQL = """INSERT INTO courses(title, code, description) VALUES (?, ?, ?);"""
        
        courses = [
            ("Comp Sci", "CS101", "learn to code"),
            ("Literature", "LIT101", "reading stuff")
                ]

        for course in courses:
            cur.execute(SQL, course)

if __name__ == "__main__":
    seed()
