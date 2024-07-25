from lib.outPutPrint import outPutPrint


def quickSort(array):
    # Write your code here.
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] > array[rightIdx]:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

    array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


data, input_data = [8, 5, 2, 9, 5, 6, 3], [8, 5, 2, 9, 5, 6, 3]
output = quickSort(data)
outPutPrint(input_data, output)
