import sqlite3
from app.orm import ORM
from app.util import hash_password
from app.util import api_key
import json

class Admin(ORM):
    tablename = "admin"
    fields = ["username", "password_hash", "api_key"]

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.api_key = kwargs.get('api_key')
   
    @classmethod
    def login(cls, username, password):
        return cls.select_one_where("WHERE username = ? AND password_hash = ?",
                                    (username, hash_password(password)))

    @classmethod
    def authenticate_api(cls,key):
        return cls.select_one_where("WHERE api_key = ?", (key,))

    def set_password(self, password):
        hashed_pw = hash_password(password)
        self.password_hash = hashed_pw 
        return hashed_pw

    def set_api_key(self):
        key = api_key()
        self.api_key = key
        return api_key