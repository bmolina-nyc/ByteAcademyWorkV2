## Word Count Database

Do each part on your own, then compare your work with your cohort-mates'. Copy their work if you need to to keep up, but attempt everything yourself.

### Part One

Design the following database schema:

* A book has a title of up to 128 characters in length, an author of up to 128 characters in length, and text content of unlimited length (a TEXT field)

* A word represents the number of times a specific word appears in a specific book. A book has many words, and there should only be an one entry for a given word in a given book.

### Part Two

Implement basic ORM subclasses for the two tables, Book and Word.

Implement the following method for Word

`def __init__(self, **kwargs)`

Implement the following method for Book

`def __init__(self, **kwargs)`

This should create `self.fieldname` fields for the columns in your two databases.

### Part Three

Create the following methods in Book

```
@classmethod
def from_title(title):
    """ return Book object for a given title in the database """

def load_text(self, filepath):
    """ load a text file's content into the book's text content """
```

### Part Four

Create a unit test test_book. Test that you can create a new book, load its texts, save it to the database, load it back from its title, and have it contain the correct text & author.

### Part Five

Create the following methods in Book

```
def generate_counts(self)
    """ first delete any existing word counts for this book to avoid double counting, then create create Word entries for each word in the text with the count for each word. """
```

    * Words should be case insensitive and contain only letters, numerals, or apostrophes. Split lines on white space or hyphens. Scrub out any characters in words that are not letters, numerals, or apostrophes. There are several ways of doing this.
