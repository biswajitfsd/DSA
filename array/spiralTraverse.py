def spiralTraverse(array):
    # Write your code here
    result = []
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


pass


def spiralFill(array, sRows, eRows, sCols, eCols, result):
    print(sRows, eRows, sCols, eCols)
    if sRows > eRows or sCols > eCols:
        return
    for col in range(sCols, eCols + 1):
        result.append(array[sRows][col])

    for row in range(sRows + 1, eRows + 1):
        result.append(array[row][eCols])

    for col in reversed(range(sRows, eCols)):
        result.append(array[eRows][col])

    for row in reversed(range(sRows + 1, eRows)):
        result.append(array[row][sCols])

    spiralFill(array, sRows + 1, eRows - 1, sCols + 1, eCols - 1, result)


payload = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

print(spiralTraverse(payload))
