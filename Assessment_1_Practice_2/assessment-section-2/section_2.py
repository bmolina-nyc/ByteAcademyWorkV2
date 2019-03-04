


def string():
    string = input("type a string")
    for word in string.split(" "):
        print(f"{word.upper()}!")

# string()

def every_other(myList):
    for el in range(0,len(myList),2):
        print(myList[el])

# every_other([1,10,100,1000,10000])

def triple_string(string):
    return ((string + " ") * 3)

# print(triple_string("Look!"))

def str_list(myList):
    return list(map(lambda x: str(x), myList))
    # return myList.map(lambda x: str(x))

# print(str_list([1,2,3,4]))

# d = {
#     'Carter': 'value',
#     'Greg': ['list', 'of', 'values'],
#     'Kenso': 'VALUE'
# }

# d['Nikhil'] = "another value"
# print(d)
# print(d['Carter'])
# print(d['Greg'][1])

# A = ord('A')
# dic = {}
# for code in range(A+25, A-1, -1):
#     letter = chr(code)
#     dic[letter] = code

# keys = sorted(dic.keys())
# for key in keys:
#     print(f"{key} {dic[key]}")

def firsttwo(string):
    if len(string) >= 2:
        print(string[0:2])
    else:
        print(string)

# firsttwo("t")

def whileTrue():
    while True:
        print('Input a string, \'done\' to quit:')
        response = input()
        if response == "done":
            print("bye!")
            return
        else:
            firsttwo(response)
            continue

whileTrue()