## Day 5 Exercise 3 - Word Count
---

##### Objective

* Write a function that takes a filename and counts the number of appearances
of each unique word. It should return a data structure that holds those counts.

`def count_words(filename):`

*   * q: when are two words the same? It's not a straightforward question.
How might you ignore non-word characters such as a comma or period or quotation
mark? You may want to write a function that takes a string and returns a string
with non-word characters and capitalization removed. Regular expressions and
the `re` library can perform much more sophisticated string analysis than
python's core string methods & operations.

* Write a second function that takes the data structure returned by the first
function that returns a structure with n words & the word's count for the n
most common words. Hint: a clever application of the `key` parameter of sort
can be used to get the keys of a dictionary sorted by their values.

`def most_common(word_counts, n):`

* Write a third function that formats your output as a neat table.

* Finally use sys.argv so that your program can be executed with
`python countwords.py filename.txt` to display the 20 most common words in
a file specified by the user. You should handle the situation where the user
specifies a non-existant file with friendlier output than a python error
message (use `try` and `except`)

