# 1) Write a program that prompts the user for three floating point numbers. It should add the first two 
# together, and then mulitply the sum by the third number. Print the result formatted so it has three 
# digits after the decimal place (such as 32.050)

def prompt_user():
    while True:
        number_a = input("Enter a floating point number ")
        number_b = input("Enter a second floating point number ")
        number_c = input("Enter one more floating point number ")


        if "." not in number_a and "." not in number_b and "." not in number_c:
            print("Please make sure all inputs are floating numbers")
            continue 
        else:
            number_a = float(number_a)
            number_b = float(number_b)
            number_c = float(number_c)
            return format((number_a + number_b) * number_c, '.3f')

# print(prompt_user())

# 2) Write a program that prompts the user for a string. It should calculate the length of that string and 
# then the number of times 5 divides that length evenly, as well as the remainder after the division.

def str_length():
    string = input("enter a string ")
    length = len(string) 
    count = 0 
    
    copy = length
    remainder =  int(length) % 5
    while copy - 5 > 0:
        if copy - 5 > 0:
            copy -= 5
            count +=1
    return f"The string length is {length} and 5 goes in {count} times and the remainder is {remainder}"

# print(str_length())

# Print the numbers from 0 to 50 with the multiples of 7 left out.

def skip_mult_7():
    for el in range(0,51):
        if el % 7 == 0:
            continue
        else:
            print(el)
# print(skip_mult_7())

def string_tests_vowel_20():
    string = input("please enter a string ")
    test_a = string[0].lower() in "aeiou"
    test_b = len(string) >= 20 

    if test_a and test_b:
        print("both tests passed")
    elif test_a or test_b:
        print("one of the tests passed")
    else:
        print("no tests passed")

string_tests_vowel_20()

def print_alpha():
    line_a = " "
    line_b = " "

    count = 1
    i = 65 
    while True:
        print(count)
        if count == 27:
            break 
        if count <= 13:
            line_a += chr(i) + " "
            i += 1
            count += 1
        if count > 13:
            line_b += chr(i) + " "
            i += 1
            count += 1
    print(line_a)
    print(line_b)

# print(print_alpha())



# `chr(65) == 'A'`, `chr(66) == 'B'`, ... , `chr(90) == 'Z'`.