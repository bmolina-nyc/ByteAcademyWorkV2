import sqlite3
from app.orm import ORM

class TodoItem(ORM):

    dbpath = "todo.db"
    tablename = "todoitems"
    fields = ['title', 'description', 'complete', 'users_pk']

    # tablename = "todoitems"

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.complete = kwargs.get('complete')
        self.users_pk = kwargs.get('users_pk')

    @classmethod
    def all_for_users_pk(cls, users_pk):
        return cls.select_many_where("WHERE users_pk = ?", (users_pk, ))

    def __repr__(self):
        return "<TodoItem: '{}' user_pk={}>".format(self.title, self.users_pk)
