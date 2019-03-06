import os 
from app.orm import ORM
from app.campuses import Campuses
from app.students import Students

DIR = os.path.dirname(__file__)
DBFILENAME = 'campus_students.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath = DBPATH):
    ORM.dbpath = dbpath

    studenta = Students(lname = "Lockett", fname="Walker", school="NYC", id="S000000001", gpa="3.1", campus_pk=1)
    studentb = Students(lname = "Coleman", fname="Casey", school="NYC", id="S000000002", gpa="2.7", campus_pk=1)
    studentc = Students(lname = "Kilome", fname="Franklyn", school="NYC", id="S000000003", gpa="3.8", campus_pk=1)
    studentd = Students(lname = "Santiago", fname="Hecton", school="NYC", id="S000000004", gpa="2.9", campus_pk=1)

    studenta.save()
    studentb.save()
    studentc.save()
    studentd.save()

    nyc = Campuses(city="NYC", state="NY")
    nyc.save()
  

    studente = Students(lname = "Valdez", fname="Framber", school="Houston", id="S000000005", gpa="3.9", campus_pk=2)
    studentf = Students(lname = "Peacock", fname="Brad", school="Houston", id="S000000006", gpa="2.8", campus_pk=2)
    studentg = Students(lname = "Guduan", fname="Reymin", school="Houston", id="S000000007", gpa="3.5", campus_pk=2)
    studenth = Students(lname = "Cole", fname="Gerrit", school="Houston", id="S000000008", gpa="3.0", campus_pk=2)

    studente.save()
    studentf.save()
    studentg.save()
    studenth.save()

    houston = Campuses(city="Houston", state="TX")
    houston.save()
  

if __name__ == "__main__":
    seed()