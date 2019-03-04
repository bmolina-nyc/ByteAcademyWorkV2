## Foundation Assessment Pt. 3

Answer 3 of the following 5 questions.

For entrance exam exemption, you must answer the last two questions.

1) Count & print out the number of lines in tothelighthouse.txt. Include the blank lines in your count.

2) Create a new text file called linecount.txt that is the length (number of characters) of every line of tothelighthouse.txt on its own line. Your file will have as many lines as the text of the book has with just a single integer per line.

3) Open aapl.json and load its data into a variable.

Create a new dictionary that only has the 'companyName', 'latestPrice', and 'marketCap'  keys and their values.

Save that dictionary to a file called 'AAPLprice.json'

4) Using the csv module, calculate the total number of flights that happened over all three years in airtravel.csv

5) This question is in two parts. If you are not trying for exemption, you only have to do the first one.

* Open lists.json and load its data into a variable.

For each key, print the key, length of the list associated with that key, and the last element of that list

```
F 6 92
D 5 32
J 6 65
H 6 65
...
```

* Create a new dictionary that has each key of lists.json. The value should itself be a dictionary with two keys. 'length' with the length of the corresponding list, and 'max' with the max value of that list. Save that dictionary to a new json file.


```
{
    'F': {
        'length': 6,
        'max': 92
    },
    'D': {
        'length': 5,
        'max': 97
    },
    ... etc
```

