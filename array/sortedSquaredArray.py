def sortedSquaredArray(array):
    n = len(array)
    squared_array = [0] * n

    # Square all elements
    for i in range(n):
        squared_array[i] = array[i] ** 2

    j = range(n)
    i = k = 0
    while i < n-1:
        if squared_array[i] > squared_array[i + 1]:
            temp = squared_array[i]
            squared_array[i] = squared_array[i + 1]
            squared_array[i + 1] = temp

        i += 1

    return squared_array


array = [1, 3, 2, 4, 8, 6, 7, 5, 9, 10]
print(sortedSquaredArray(array))
