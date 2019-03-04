from app.orm import ORM
import sqlite3 
import csv
import os
from app.word import Word

DIRNAME = os.path.dirname(__file__)
DBFILENAME = 'books_words.db'
TXTFILENAME = 'mobydick.1.txt'
DBPATH = os.path.join(DIRNAME, DBFILENAME)
TXTPATH = os.path.join(DIRNAME, TXTFILENAME)

class Book(ORM):
    tablename = 'books'
    fields = ['title', 'text_content', 'author']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.title = kwargs.get('title')
        self.text_content = kwargs.get('text_content')
        self.author = kwargs.get('author')

    @classmethod
    def from_title(cls, title):
        # result = cls.select_one_from("WHERE title = ?", (title,))
        # print(result)
        return cls.select_one_from("WHERE title = ?", (title,))
    """ return Book object for a given title in the database """


    def load_text(self, dbname='books_words.db'):
        characters_to_exclude = ['\n', ".", '“', '”', ',', ":", " ", ";", "*", "(", ")", "'", "[", "]", "#","'\n '"]
        with open(TXTPATH, 'r') as file, sqlite3.connect(dbname) as conn:
            lines = file.readlines()
            text = ""
            for line in lines:
                words_to_parse = line.split(" ")
                for word in words_to_parse:
                    parsed_word = "".join(char for char in word if char not in characters_to_exclude)
                    text += " " + parsed_word
                
            self.text_content = text.strip()
            self._update()
            self.save()
            return self.text_content
            """ load a text file's content into the book's text content """
   
    def generate_counts(self):
        word_dic = {}
        words = self.load_text()
        for word in words.split(" "):
            if word.lower() in word_dic:
                word_dic[word.lower()] += 1
            else:
                word_dic[word.lower()] = 1

        for word, total in word_dic.items():
            word_check = Word.select_one_from("WHERE word = ?", (word,))
            # print(word_check)
            if word_check is None:
                word_count = Word(books_pk = self.pk, word=word, word_count= total)
                word_count.save()
                
        """ first delete any existing word counts for this book to avoid double 
        counting, then create create Word entries for each word in the text 
        with the count for each word. 
        * Words should be case insensitive and contain only letters, numerals, or 
        apostrophes. Split lines on white space or hyphens. Scrub out any characters 
        in words that are not letters, numerals, or apostrophes. There are several ways of doing this."""

