import os
from app.orm import ORM
from app.book import Book
from app.word import Word 

DIR = os.path.dirname(__file__)
DBFILENAME = 'books_words.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    word = Word(books_pk=1, word="Testing", word_count=50)
    word.save()
    
    book = Book(title="A good book", text_content="Once upon a time...", author="Kevin Johnson")
    book.save()

    


    # mike_bloom = Account(username='mike_bloom', balance=10000.00)
    # mike_bloom.set_password('password')
    # mike_bloom.save()
