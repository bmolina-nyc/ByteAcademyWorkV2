import sqlite3
from app.orm import ORM


class Employee(ORM):
    tablename = "employees"
    fields = ["branches_pk", "fName", "lName", "title", "dob"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.branches_pk = kwargs.get('branches_pk')
        self.fName = kwargs.get('fName')
        self.lName = kwargs.get('lName')
        self.title = kwargs.get('title')
        self.dob = kwargs.get('dob')