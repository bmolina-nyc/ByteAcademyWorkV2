import sqlite3
import os
import unittest
from app.todoitem import TodoItem
from seed import seed
from schema import schema

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)


class TestTodoItem(unittest.TestCase):
    def setUp(self):
        """ the setup method must be called setup """
        TodoItem.dbpath = DBPATH
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        """ the tear down method must be called tearDown """
        os.remove(DBPATH)

    def test_save_insert(self):
        vals = {
            'title': 'Read A Book',
            'description': 'Read It',
            'complete': 1,
            'users_pk': 999
        }
        read_book = TodoItem(**vals)

        read_book.save()

        with sqlite3.connect(DBPATH) as conn:
            cur = conn.cursor()
            cur.execute(""" SELECT COUNT(*) FROM todoitems WHERE 
title='Read A Book' AND description='Read It' AND 'complete'=1 AND 'users_pk'=999; """
                        )
            nresults = len(cur.fetchall())

        self.assertEqual(nresults, 1,
                         'save creates a db entry with filled values')

        with sqlite3.connect(DBPATH) as conn:
            cur = conn.cursor()
            cur.execute(""" SELECT pk FROM todoitems WHERE 
title='Read A Book';""")

            new_pk = cur.fetchone()[0]

        self.assertGreaterEqual(new_pk, 1, 'save fills new pk value')

    def test_save_update(self):
        return  # remove this to run the test
        vals = {
            'title': 'Clean up room',
            'description': 'Clean it up',
            'complete': 0,
            'users_pk': 1000
        }

        clean_room = TodoItem(**vals)

        clean_room.description = 'At least put away your clothes'
        clean_room.complete = 1

        clean_room.save()

        with sqlite3.connect(DBPATH) as conn:
            cur = conn.cursor()
            cur.execute(""" SELECT pk FROM todoitems WHERE 
title='Clean up room';""")
            nitems = len(cur.fetchall())

        self.assertEqual(nitems, 1, 'save only inserts once')

        with sqlite3.connect(DBPATH) as conn:
            cur = conn.cursor()
            cur.execute(""" SELECT description, complete FROM todoitems WHERE 
title='Clean up room';""")
            desc_complete = cur.fetchone()

        self.assertEqual(desc_complete, ('At least put away your clothes', 1),
                         'save updates values in existing item')

    def test_one_from_pk(self):
        item1 = TodoItem.one_from_pk(1)
        self.assertEqual(item1.pk, 1, "pk is set")
        self.assertEqual(item1.title, "Item 1", "title is set")
        self.assertEqual(item1.description, "Do A Thing", "description is set")
        self.assertEqual(item1.complete, 0, "complete is set")
        self.assertEqual(item1.users_pk, 1, "users_pk is set")
