import sqlite3
from app.orm import ORM


class Branch(ORM):
    tablename = "branches"
    fields = ["branchName","city", "state", "zip"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.branchName = kwargs.get('branchName')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.zip = kwargs.get('zip')