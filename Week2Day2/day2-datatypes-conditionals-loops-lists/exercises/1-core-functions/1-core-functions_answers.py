# print() # and the file, end, and sep parameters

# input()
''' input() prompts the user to enter a value - the value is always a string
The value will be saved to a variable you assigned to it

my_var = input("give me a number") # user enters 5

print(my_var) # console prints 5
type(my_var) # the 5 is from the str class
'''


# # the .is methods of strings (isalpha() isalnum() etc)
'''
these functions allow a user to check if a character is of the types a-z 
or A-Z (for isalpha() or also 0-9 (for isalnum()). 
This is very useful if you wanted to filter out only these specific characters and
nothing else when parsing a string or just to check if the string is of the types 
listed above.

str_a = "this is not alphanumeric cause there are spaces"
print(str_a.isalnum())  # returns False

str_b = "alphastring"
print(str_b.isalpha()) # returns True

str_c ="abc123"
print(str_c.isalnum()) # returns True
'''


# math.isclose() # look at (.1 + .2) == .3
# round()
# len()
# sum()