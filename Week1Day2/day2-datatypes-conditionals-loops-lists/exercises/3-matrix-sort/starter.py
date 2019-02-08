def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """

    with open(filename, 'r') as input_file:
        items =  [[int(column) for column in row.split()] for row in input_file]
        return items

dataset = read_matrix("testmatrix0.txt")


def rows_summer(dataset):  
        row_sums = []
        for i in range(len(dataset)): 
                for j in dataset:
                        row_sums.append(sum(dataset[i]))
                        break

        print("Row Sums: " +  " ".join(map(lambda i: str(i), row_sums)))

    
# def columns_summer(dataset):
#         column_sums_math = []
#         final_column_sums = []

#         for idx in range(len(dataset)+1):
#                 for list_el in dataset:
#                         column_sums_math.append(list_el[idx])
#                         if len(column_sums_math) == len(dataset):
#                                 final_column_sums.append(sum(column_sums_math))
#                                 column_sums_math = []
#         print('Columm Sums: ' + " ".join(map(lambda x: str(x), final_column_sums)))

# def columns_summer(dataset):
#     final_column_sums = [sum([row[i] for row in dataset]) for i in range(0, len(dataset[0]))]
#     print('Columm Sums: ' + " ".join(map(lambda x: str(x), final_column_sums)))

def columns_summer(dataset):
    column_sums = [] 
    for i in range(len(dataset[0])):
        sum = 0
        for data_list in dataset:
            sum += data_list[i] # an individual indexed item from each list
        column_sums.append(sum)     
    print('Column Sums: ' + " ".join(map(lambda x: str(x), column_sums)))

def matrix_sort_rows(dataset):
        for i in range(len(dataset)):
                for j in range(len(dataset)-1):
                        if sum(dataset[j]) > sum(dataset[j+1]):
                                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
        for inner_list in dataset:
                print(" ".join(map(lambda x: str(x), inner_list)))

def matrix_sort_columns(dataset):
        pass


              
# rows_summer(dataset)
# columns_summer(dataset)
# matrix_sort_rows(dataset)
matrix_sort_columns(dataset)