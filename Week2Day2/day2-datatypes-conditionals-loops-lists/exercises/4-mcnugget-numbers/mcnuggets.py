def mcnuggets(y):
    six, nine, twenty = 6,9,20

    x = {} 
    for i in range(10):
        for j in range(10):
            for k in range(10):
                # get the total sum of every number in the ranges multiplied by nugget amount
                total = k * six + j * nine + i * twenty
                # create a dictionary key and value pair for the total and the number of nugget 
                # combos it takes to create the total
                x[total] = [f'six: {k}, nine: {j}, twenty: {i}']
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
 

mcnuggets(45)
