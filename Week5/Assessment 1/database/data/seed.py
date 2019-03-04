import os 
from app.orm import ORM
from app.campuses import Campuses
from app.students import Students

DIR = os.path.dirname(__file__)
DBFILENAME = 'campus_students.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath = DBPATH):
    ORM.dbpath = dbpath

    studenta = Students(lname = "Lockett", fname="Walker", school="NYC", id="S000000001", gpa="3.1")
    studentb = Students(lname = "Coleman", fname="Casey", school="NYC", id="S000000002", gpa="2.7")
    studentc = Students(lname = "Kilome", fname="Franklyn", school="NYC", id="S000000003", gpa="3.8")
    studentd = Students(lname = "Santiago", fname="Hecton", school="NYC", id="S000000004", gpa="2.9")

    studenta.save()
    studentb.save()
    studentc.save()
    studentd.save()

    nyca = Campuses(student_pk=1, city="NYC", state="NY")
    nycb = Campuses(student_pk=2, city="NYC", state="NY")
    nycc = Campuses(student_pk=3, city="NYC", state="NY")
    nycd = Campuses(student_pk=4, city="NYC", state="NY")

    nyca.save()
    nycb.save()
    nycc.save()
    nycd.save()

    studente = Students(lname = "Valdez", fname="Framber", school="Houston", id="S000000005", gpa="3.9")
    studentf = Students(lname = "Peacock", fname="Brad", school="Houston", id="S000000006", gpa="2.8")
    studentg = Students(lname = "Guduan", fname="Reymin", school="Houston", id="S000000007", gpa="3.5")
    studenth = Students(lname = "Cole", fname="Gerrit", school="Houston", id="S000000008", gpa="3.0")

    studente.save()
    studentf.save()
    studentg.save()
    studenth.save()

    houstona = Campuses(student_pk=5, city="Houston", state="TX")
    houstonb = Campuses(student_pk=6, city="Houston", state="TX")
    houstonc = Campuses(student_pk=7, city="Houston", state="TX")
    houstond = Campuses(student_pk=8, city="Houston", state="TX")

    houstona.save()
    houstonb.save()
    houstonc.save()
    houstond.save()


if __name__ == "__main__":
    seed()