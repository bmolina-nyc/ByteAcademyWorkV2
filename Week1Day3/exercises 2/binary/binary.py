
import math 
def binary(n):
    remainders = []
    while True:
        remainder = n % 2
        remainders.append(remainder)
        n /=2
        if n < 1:
            break
    remainders.reverse()
    binary_nums = map(lambda el: math.floor(el), remainders) # takes out any floating decimals from the 0's and 1's
    return "".join(map(lambda el: str(el), binary_nums )) # turns the list of 0s and 1s into a string format


print(binary(10))