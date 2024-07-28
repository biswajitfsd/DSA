from lib.outPutPrint import outPutPrint


def searchInSortedMatrix(matrix, target):
    # Write your code here.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return [i, j]
    return [-1, -1]


def searchInSortedMatrix_v2(matrix, target):
    # Write your code here.
    i = 0
    j = 0
    no_of_rows = len(matrix)
    no_of_cols = len(matrix[0])
    while i < no_of_rows and j < no_of_cols:
        if matrix[i][j] == target:
            return [i, j]
        if matrix[i][j] > target:
            no_of_cols -= 1
        if j >= no_of_cols - 1:
            i += 1
            j = 0
        else:
            j += 1

    return [-1, -1]


data = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]
target = 33
output = searchInSortedMatrix_v2(data, target)

outPutPrint(data, output)
