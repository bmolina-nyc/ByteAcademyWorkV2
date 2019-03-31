import os 
from app.orm import ORM
from app import Branch, Employee, Admin 

DIR = os.path.dirname(__file__)
DBFILENAME = 'bank.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    citibank = Branch(branchName="Citibank", city="New York City", state="NY", zip=10003)
    applebank = Branch(branchName="Apple Bank", city="New York City", state="NY", zip=10004)
    tdbank = Branch(branchName="TDbank", city="Boston", state="MA", zip=12345)

    bruce = Employee(branches_pk = 1, fName="Bruce", lName="M", title="Boss", dob="8/7/81")
    john = Employee(branches_pk = 2, fName="John", lName="S", title="Underling", dob="12/11/81")
    tom = Employee(branches_pk = 3,fName="Tom", lName="Q", title="Comedian", dob="5/6/81")
    cait = Employee(branches_pk = 1, fName="Cait", lName="D", title="Lady" , dob="10/3/86")
    kes = Employee(branches_pk = 2, fName="Kes", lName="S", title="Underling", dob="12/1/82")
    zoe = Employee(branches_pk = 3,fName="Zoe", lName="H", title="Dancer", dob="6/2/82")

    citibank.save()
    applebank.save()
    tdbank.save()

    bruce.save()
    john.save()
    tom.save()
    cait.save()
    kes.save()
    zoe.save()

    bruce = Admin(username='bruce')
    bruce.set_password('password')
    bruce.api_key = '12345'
    bruce.save()
