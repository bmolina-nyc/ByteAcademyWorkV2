def sorting(MyList):
    zero_count = MyList.count(0)
    list_check = MyList.count(0)
    check = []
    while zero_count > 0:
        check.append(0)
        zero_count -= 1
    while True:
        for el in MyList:
            if el == 0:
                idx = MyList.index(el)
                pop = MyList.pop(idx)
                MyList.append(pop)
                print(check)
                print(MyList)
                input()
            elif el != 0:
                continue   
            if MyList[-list_check:] == check:
                return MyList
            else:
                continue

# print(sorting([1, 0, 7, 2, 0, 3, 9, 0, 4]))
# [1, 7, 2, 3, 9, 4, 0, 0, 0]

if __name__ == "__main__":
    print(sorting([1, 0, 7, 2, 0, 3, 9, 0, 4]))