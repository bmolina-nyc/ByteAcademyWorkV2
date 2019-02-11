roman_nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (8, 'VIII'), (7, 'VII'), (6,'VI'), (5, 'V'), (4, 'IV'),(3,'III'), (2, "II"), (1, 'I')]

# # only works relative to the translated numeric digits above

# def roman_numerals(number):
#     stringified_number = str(number)
#     numbers = []
#     roman_numbers = []
#     i = 0
#     while i < len(stringified_number):
#         if stringified_number[i] == "0":
#             i += 1
#         elif (i+1) == len(stringified_number):
#             numbers.append(stringified_number[i])
#             i+=1
#         else: 
#             numbers.append(stringified_number[i] + len(stringified_number[i+1:]) * "0" )
#             i += 1

#     for el in numbers:
#         for tup in roman_nums:
#             if int(el) == tup[0]:
#                 roman_numbers.append(tup[1])

#     return "".join(roman_numbers)


def roman_numifier(num):
    
    roman = ''

    while num > 0:
        for i, r in roman_nums:
            while num >= i:
                roman += r
                num -= i

    return roman

print(roman_numifier(2019))

    
# print(roman_numerals(449))
