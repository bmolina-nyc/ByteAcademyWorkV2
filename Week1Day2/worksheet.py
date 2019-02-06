from random import randint
from functools import reduce 

# random numbers in a range of 20 numbers
randlist = [randint(-99,0) for _ in range(20)]

print(sorted(randlist, key=abs))

# abs(-5) --> 5
# map
# filter
# reduce

map_object = map(lambda n: n * 100, randlist)

# list comprehension
new_list = [n * 100 for n in randlist]

print(list(new_list))

def is_even(n):
    if n % 2 == 0:
        return True
    return False 

filter_object = filter(is_even, randlist)
print(list(filter_object))

# list comprehension
filtered_list = [n for n in randlist if n % 2 == 0]

print(filtered_list)


# # reduce 
def mysum(a, b):
    return a + b 

print(reduce(mysum, randlist, 0))