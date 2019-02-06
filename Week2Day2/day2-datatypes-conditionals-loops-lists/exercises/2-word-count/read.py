
import operator
file_object = open("article.txt", "r")

def word_counter(file_object, n):
    words_dic = {}
    words_list = [word for line in open("article.txt", "r") for word in line.split()]

    for word in words_list:
        if word.isalpha():
            if word in words_dic:
               words_dic[word] += 1
            else:
                words_dic[word] = 1

    sorted_words_dic = sorted(words_dic.items(), reverse=True, key=operator.itemgetter(1) )
    print(sorted_words_dic)
    
    counter = n 
    while counter > 0:
        for key,value in sorted_words_dic:
            print(key, value)
            counter -= 1
            if counter == 0:
                break
    
word_counter("file_object", 5)