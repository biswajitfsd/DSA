from lib.outPutPrint import outPutPrint


# Best Solution
def selectionSort(array):
    n = len(array)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if array[j] < array[smallest_index]:
                smallest_index = j

        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array


# First Solution
# def selectionSort(array):
#     # Write your code here.
#     i = 0
#     j = len(array)
#     smallest_index = 0
#     shorting_index = 0
#     while i < j:
#         if smallest_index < j and array[i] < array[smallest_index]:
#             smallest_index = i
#
#         i += 1
#         if i == j:
#             array[smallest_index], array[shorting_index] = array[shorting_index], array[smallest_index]
#             if smallest_index < j:
#                 shorting_index += 1
#                 smallest_index = shorting_index
#                 if shorting_index < j:
#                     i = shorting_index
#
#     return array


array = [8, 5, 2, 9, 5, 6, 3]
output = selectionSort(array)
outPutPrint(array, output)

array = [1, 2, 3]
output = selectionSort(array)
outPutPrint(array, output)
