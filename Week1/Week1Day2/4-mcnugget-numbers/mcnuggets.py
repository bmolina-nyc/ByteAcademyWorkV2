def mcnuggets(y):
    six, nine, twenty = 6,9,20

    x = {} 
    for i in range(y):
        for j in range(y):
            for k in range(y):
                # get the total sum of every number in the ranges multiplied by nugget amount
                total = i * six + j * nine + k * twenty
                # create a dictionary key and value pair for the total and the number of nugget 
                # combos it takes to create the total
                x[total] = [f'six: {i}, nine: {j}, twenty: {k}']
                # created entire dictionary, now bubbling up to check if any total matches the
                # passed in parameter. If so, we'll also share the key,value pair from the dictionary
                if y == total:
                    print(f"True - {y} can be made via {x[y]}")
                    return True 
            if y == total:
                print(f"True - {y} can be made via {x[y]}")
                return True 
        if y == total:
            print(f"True - {y} can be made via {x[y]}")
            return True 
    print("Not a mcnugget number")
    return False 
 

mcnuggets(20)
