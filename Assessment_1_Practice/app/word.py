from app.orm import ORM

class Word(ORM):
    tablename = 'words'
    fields = ['books_pk', 'word', 'word_count']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.books_pk = kwargs.get('books_pk')
        self.word = kwargs.get('word')
        self.word_count = kwargs.get('word_count')
