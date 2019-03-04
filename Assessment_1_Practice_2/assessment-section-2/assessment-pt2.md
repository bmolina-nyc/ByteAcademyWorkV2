## Foundation Assessment, Pt. 2

Answer 3 of the following questions

If you are attempting to exempt the entrance requirements for Byte, you must attempt one of the final two questions.

1) Input a string from the user. Break the string into words and then print each word in all caps followed by a '!'

```
Input a string: Some data for the question

SOME
DATA
FOR
THE
QUESTION
```

2) This question is in three parts. Each part requires you to write a function.

* Write a function that returns every other element of a list.

```
every_other([1,10,100,1000,10000])

# returns:

[1, 100, 10000]
```

* Write afunction that takes a string as an argument returns a new string 
    that is that string repeated 3 times.

```
triple_string("Look! ")

# returns

'Look! Look! Look!'
```

* Write a function that takes a list of numbers and returns a list of those 
    converted to strings

```
str_list([1,2,3,4])

# returns

['1', '2', '3', '4']
```

3) This question is in three parts and uses the following starter code:

```
d = {
    'Carter': 'value',
    'Greg': ['list', 'of', 'values'],
    'Kenso': 'VALUE'
}
```

* Add the key 'Nikhil' with the string 'another value' as its value to the 
dictionary.

* Print the value referenced by the key 'Carter'

* Print the second element of the list value indexed by 'Greg'

4) Use the following code to complete this problem:

```
A = ord('A')
dic = {}
for code in range(A+25, A-1, -1):
    letter = chr(code)
    dic[letter] = code
```

Don't modify this code, you will just be using the dictionary stored in the
variable `dic`.

Use a loop to print each key in dic followed by its value. The order of the keys does not matter.

```
F 70
G 71
I 73
M 77
J 74
E 69
C 67
Y 89
...
```

* BONUS: Print the key, value pairs with the keys in alphabetical order.

```
A 65
B 66
C 67
...
```


5) This question is in two parts.

* Write a function that takes a string as its argument and returns a string
    that is the first two letters of the argument string. If the string is less 
    than two characters, return the string as it is.

```
x = firsttwo('Test')
print(x)
Te

y = firsttwo('Y')
print(y)
Y
```

* Create an input loop asking the user to input strings until they input 'done'. After they have finished, Print out each element of that list on its own line.

```
Input a string, 'done' to quit: Carter
Input a string, 'done' to quit: Greg
Input a string, 'done' to quit: Kenso
Input a string, 'done' to quit: Nikhil
Input a string, 'done' to quit: done

Ca
Gr
Ke
Ni
```
