
with open('test.txt', 'r') as file_object:
    for line in file_object:
        print(line.split())

print('\n\n\n\n')

with open('test.txt', 'r') as file_object:
    line = file_object.readline()
    print(line)
    line2 = file_object.readline()
    print(line2)

print('\n\n\n\n')

with open('test.txt', 'r') as file_object:
    whole_text = file_object.read()
    print(whole_text)

with open('file_open_with.py') as file_object:
    for line in file_object:
        print(line, end='')
