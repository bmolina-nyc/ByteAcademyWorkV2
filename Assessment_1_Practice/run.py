#! /usr/bin/env python3
import os
from app.orm import ORM
from app import controller
from app.book import Book
DIR = os.path.dirname(__file__)
DBFILENAME = 'books_words.db'
DBPATH = os.path.join(DIR, 'data', DBFILENAME)
DIRNAME = os.path.dirname(__file__)
CSVFILENAME = 'mobydick.1.txt'
CSVPATH = os.path.join(DIRNAME, CSVFILENAME)

import os
# # from app.orm import ORM
# # from app import controller



# # child classes default to ORM'm dbpath if it is not set
ORM.dbpath = DBPATH
# controller.run()
b = Book(title="Moby Dick", author = "Moby Dicks Author")
b.from_title("A good book")
b.load_text()
b.generate_counts()
b.generate_counts()

