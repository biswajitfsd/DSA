def transposeMatrix(matrix):
    # Write your code here.
    length = len(matrix)
    breath = len(matrix[0])
    new_matrix = [[0] * length for i in range(breath)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


matrix = [
    [1, 2]
]
print(transposeMatrix(matrix))
