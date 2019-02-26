import sqlite3
from app.todoitem import TodoItem
from app.orm import ORM


class User(ORM):

    dbpath = "todo.db"
    tablename = "users"
    fields = ['username', 'pin']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.pin = kwargs.get('pin')

    def get_todo_items(self):
        return TodoItem.all_for_users_pk(self.pk)

    def add_todo_item(self, **kwargs):
        # create a new item, maybe set from kwargs
        newitem = TodoItem(**kwargs)
        # attach that item to this user
        newitem.users_pk = self.pk
        # save the new item
        newitem.save()


    @classmethod
    def login(cls, username, pin):
        return cls.select_one_from("WHERE username = ?, pin = ?", (username, pin))

    