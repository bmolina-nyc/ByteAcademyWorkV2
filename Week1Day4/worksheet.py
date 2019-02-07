# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/tutorial/inputoutput.html
# https://docs.python.org/3/library/csv.html


# #open a file, pass file name, 
# file_object = open('test.txt', 'r')


# add the extra parameter end="" to kill the automatic newline characters
# for line in file_object:
#     print(line, end="")

# # # close a file 
# file_object.close()

# # file_open_with.py

# with open('test.txt', 'r') as file_object:
#     for line in file_object:
#         print(line, end="")

# with open('test.txt', 'r') as file_object:
#     for line in file_object:
#         print(line.split())

# print('\n\n\n\n\n\n\n')

# with open('test.txt', 'r') as file_object:
#     for line in file_object:
#         print(line.split())

# print('\n\n\n\n\n\n\n')

# with open('test.txt', 'r') as file_object:
#     line = file_object.readline()
#     print(line)


# print('\n\n\n\n\n\n\n')



# with open('test.txt', 'r') as file_object:
#     whole_text = file_object.read()
#     print(whole_text)



# # write a file - "w" for write or "a" for append

with open("outputfile.txt", "w") as file_object:
    file_object.write("first string \n")
    file_object.write("second string \n")
    file_object.write("third string \n")


with open("outputfile2.txt", "w") as file_object:
    print("first string", file=file_object)
    print("second string", file=file_object)

# append mode
with open("outputfile3.txt", "a") as file_object:
    print("third line", file=file_object)

# csv functionality 
import csv 

