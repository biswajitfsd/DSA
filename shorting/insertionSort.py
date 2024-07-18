from lib.outPutPrint import outPutPrint


def insertionSort(array):
    # Write your code here.
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


array_p = [8, 5, 2, 9, 5, 6, 3]
output = insertionSort(array_p)
outPutPrint(array_p, output)
