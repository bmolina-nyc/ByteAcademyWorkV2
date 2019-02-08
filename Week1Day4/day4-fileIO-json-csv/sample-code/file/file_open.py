
file_object = open('test.txt', 'r')

for line in file_object:
    print(line, end='')

file_object.close()
