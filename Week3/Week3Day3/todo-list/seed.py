import os
from app.todoitem import TodoItem
# from app.user import User

DIR = os.path.dirname(__file__)
DBFILENAME = "todo.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    TodoItem.dbpath = dbpath

    td1 = TodoItem(title="Item 1", description="Do A Thing", complete=0, users_pk=1)

    td2 = TodoItem(
        title="Item 2", description="Another Thing", complete=1, users_pk=1)

    td1.save()
    td2.save()

if __name__ == "__main__":
    seed()
