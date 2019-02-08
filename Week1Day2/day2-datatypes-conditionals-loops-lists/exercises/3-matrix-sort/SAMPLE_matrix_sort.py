from tabulate import tabulate

def matrix_sort(text_file):
    with open(text_file) as f:
        text = f.readlines()

    matrix = []
    for line in text:
        matrix.append(list(map(int, line.split())))

    row_sum = []
    for i in range(len(matrix)):
        row_sum.append(sum(matrix[i]))

    col_sum = []
    for j in range(len(matrix[0])):
        x = 0
        for i in range(len(matrix)):
            x += matrix[i][j]
        col_sum.append(x)

    row_sum_enumerate = list(enumerate(row_sum))
    row_sum_enumerate = sorted(row_sum_enumerate, key=lambda x: x[1])

    sorted_by_row = []
    for i in range(len(row_sum)):
        sorted_by_row.append(matrix[row_sum_enumerate[i][0]])

    col_sum_enumerate = list(enumerate(col_sum))
    col_sum_enumerate = sorted(col_sum_enumerate, key=lambda x: x[1])

    sorted_by_col = [[] for i in range(len(matrix))]

    for j in range(len(col_sum)):
        for i in range(len(matrix)):
            sorted_by_col[i].append(matrix[i][col_sum_enumerate[j][0]])

    print(tabulate(sorted_by_row))
    print(tabulate(sorted_by_col))

matrix_sort("testmatrix.txt")


