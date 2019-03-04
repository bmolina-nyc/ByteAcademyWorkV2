## Byte Academy Phase 1 Assessment

### Part A: Questions

#### API to json

* Write a program that asks the user to input a stock ticker symbol. The program should download the chart data for that stock from IEX <https://iextrading.com/developer/docs/#chart> and save that data to a json file called "SYMBOL_chart.json" where SYMBOL is the stock ticker's symbol (tsla_chart.json, aapl_chart.json, etc.)

* The .json file should be saved in the same directory as the code for the program, regardless of where the python interpreter is executed (i.e., use the path functions we have been using for file paths & directories.)

#### Data plot

* Load the Winemag csv data into a Pandas dataframe and create a scatter plot with x = price and y = points for ONLY the US wines. Save your work to a jupyter ipynb.

#### Database

Using python's sqlite3 module write a schema.py file that creates two database tables modeling the following:

    * Campuses: A campus has a city and a state.

    * Students: A student has a first name, a last name, and a GPA,

A campus has many students, a student has one campus.

    * In a seed.py file, write sqlite3 code to add two campuses for New York, NY and Houston, TX to the database. Insert the following students:

```
first, last, id, GPA

In New York, NY:

Lockett, Walker, S000000001, 3.1
Coleman, Casey, S000000002, 2.7
Kilome, Franklyn, S000000003, 3.8
Santiago, Hecton, S000000004, 2.9

In Houston, TX:

Valdez, Framber, S000000005, 3.9
Peacock, Brad, S000000006, 2.8
Guduan, Reymin, S000000007, 3.5
Cole, Gerrit, S000000008, 3.0
```

    * Write a SQL statement to move Gerrit Cole to New York in your code.

    * Write a SQL SELECT statement to get the student ids of all students in New York with a GPA over 3.0.

#### Algorithm

* Write a function without using `sort` or `sorted`
that shifts all of the zeros in a list to the end. Do not create
a new list, alter the list as it is given by swapping values.

```
the_list = [1, 0, 7, 2, 0, 3, 9, 0, 4]

zero_sort(the_list)

print(the_list)

[1, 7, 2, 3, 9, 4, 0, 0, 0]
```

#### Terminal Trader (counts as two qeustions)

* Modify your Terminal Trader so that accounts have an `api_key` column. This should be a random string of numbers and/or letters that is 15 characters long. Accounts should receive them when a new account is created.

* The user should be able to view their api key in the user interface after logging in with a new option in the main menu. Maintain proper separation of concerns between the model, the views, and the controller.

* Create an `Account.api_authenticate(key)` class method that returns None if no account in the table has a key or the appropriate account object if the key is there. (It should be very similar to the class method that authenticates via username and password.)

* Write at least one unit test to test key creation and/or authentication.

#### Submission

* Create a new repository on github and push your work to it, submit the link.

* Proper submission is a bonus half-question.


#### Good luck, you can do it!

* Thanks for a great phase 1!
