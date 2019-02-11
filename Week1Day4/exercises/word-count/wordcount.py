import re 
import string

#items to parse out of a word
characters_to_exclude = ['\n', ".", '“', '”', ',', ":", "—"]

def count_words(filename):
    words = {}
    with open(filename, 'r') as word_file:
        for line in word_file:
            for word in line.split(" "):              
                new_word = ''.join(char for char in word if char not in characters_to_exclude)
                if new_word in words:
                    words[new_word] += 1
                else:
                    words[new_word] = 1
    return words

#based on n, returns top n most common words
def most_common(word_data_structure, n):
    sorted_list = sorted(word_data_structure.items(), key= lambda x:x[1], reverse=True)
    result = []
    for x in range(0,n):
        result.append(sorted_list[x])
    return result

def table_print(dataset):            
    print("Most Common Words")            
    print("Word Total")
    for tup in dataset:
        print("----------")
        print(f"{tup[0]} : {tup[1]}")


filename = input("what file would you like to run?: ")
count = input("tell me how many words you would like to count?: ")

class InvalidFileError(Exception):
    pass

while True:
    try:
        with open(filename, 'r') as file_object:
            if file_object:
                word_data_structure = count_words(filename)
                output_most_common = most_common(word_data_structure, int(count))
                table_print(output_most_common)
                break
    except InvalidFileError:
        print("This is not a valid file - please try again")
        print()






