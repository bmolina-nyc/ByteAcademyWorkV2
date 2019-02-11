import re
words = ["Castle", "soCal", "Basic", "castle", "X", "Waaaaay"]

for word in words:
    """match a string that has a capital letter followed by at least one 'a' at the beginning """

    """ a 'raw string' does not use escape characters, so \ is just itself. it is good practice to always use them for regular expressions."""

    """ re.search looks for a match anywhere in a string, re.match looks only at the start of the string. search can act like match if you use the ^ start of string anchor. I always use search """

    match = re.search(r'^[A-Z]a+', word)
    print("For {:<8} match, match.span(), match.groups(), and match.match".format(word))
    if match:
        print(match.group())
        print(match.span())
    else:
        print("No match")
    print()


phonenums = ["706-555-1234", "+12123678548", "23-123-7890"]

print()
print()

for phonenum in phonenums:
    pattern = r'(\d{3})-?(\d{3})-?(\d{4})$'
    match = re.search(pattern, phonenum)
    print()
    print("Matching with r'{}'".format(pattern))
    print("For {:<15}, match, match.span(), match.group(), match.groups()".format(phonenum))
    if match:
        print(match.groups())
        print(match.span())
    else:
        print("No match")
    print()

print()
print()

""" find all instances of a pattern """
pattern = r'-?\d+\.?\d*'
string = '12 people in 100 places with 9 pets at -7 degrees listening to radio station 102.7'
print("searching for '{}' in {}".format(pattern, string))
print(re.findall(pattern, string))

""" search and replace """
string = 'firstname=Carter lastname=Adams'
pattern = r'\w*name='
print(re.sub(pattern, '', string))
