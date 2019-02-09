# Open a file and set it up to read line by line

def read_file(filename):
    file_object = open(filename, 'r')
    lines = " "
    for line in file_object:
        lines += line
    print(len(lines))
    print(lines)


print(read_file('article.txt'))