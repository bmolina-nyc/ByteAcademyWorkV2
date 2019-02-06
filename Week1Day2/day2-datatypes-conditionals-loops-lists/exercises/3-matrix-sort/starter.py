def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """

    with open(filename, 'r') as input_file:
        items =  [[int(column) for column in row.split()] for row in input_file]
        # row_sums = []
        # column_sums = []
        # for i in range(len(items)):
        #         for j in items:
        #                 row_sums.append(sum(items[i]))
        #                 break

        # print("Row Sums: " +  " ".join(map(lambda i: str(i), row_sums)))

        # i = 0
        # while i < len(items[0]):
        #         column_sums.append(items[0][i] + items[1][i] + items[2][i])
        #         i += 1
        
        # print("Column Sums: " + " ".join(map(lambda i: str(i), column_sums)))

        for el in range(len(items)):
                for row in items:
                        print(row[el])


   

read_matrix("testmatrix0.txt")