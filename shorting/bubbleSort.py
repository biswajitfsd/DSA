from lib.outPutPrint import outPutPrint


# Best Solution
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array


# First Solution
# def bubbleSort(array):
#     # Write your code here.
#     n = len(array)
#     i = 0
#     array_shorted = True
#     while i < n:
#         if i + 1 < n and array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#             array_shorted = False
#
#         i += 1
#         if array_shorted is False and i == n:
#             array_shorted = True
#             i = 0
#
#     return array


array = [9, 2, 3, 4, 5, 6, 7, 8, 1]

output = bubbleSort(array)
outPutPrint(array, output)
