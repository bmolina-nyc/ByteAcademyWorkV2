from random import randint

# list comprehension version
unsorted_list = [ randint(0, 99) for _ in range(30) ]



unsorted_list_two = []
for i in range(30):
    unsorted_list_two.append(randint(0,99))

# print(unsorted_list)

# print(unsorted_list_two)

def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]


print(unsorted_list)

bubble_sort(unsorted_list)

print(unsorted_list)