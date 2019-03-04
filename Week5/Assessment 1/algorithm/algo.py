def sorting(MyList):
    result = [] 
    zeroes = []
    for el in MyList:
        if el != 0:
            result.append(el)
        else:
            zeroes.append(el)
    return result + zeroes

print(sorting([1, 0, 7, 2, 0, 3, 9, 0, 4]))
# [1, 7, 2, 3, 9, 4, 0, 0, 0]