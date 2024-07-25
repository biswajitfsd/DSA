from lib.outPutPrint import outPutPrint


def binarySearchOptimal(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
        elif array[mid] == target:
            return mid

    return -1


def binarySearch(array, target):
    # Write your code here.
    sorted_array = sorted(array)
    length = len(sorted_array) - 1
    index = binarySearchHelper(array, target, 0, length)
    return index


def binarySearchHelper(array, target, startIdx, endIdx):
    if startIdx > endIdx: return -1
    mid = (startIdx + endIdx) // 2
    if array[mid] == target:
        return mid
    if target > array[mid]:
        return binarySearchHelper(array, target, mid + 1, endIdx)
    if target < array[mid]:
        return binarySearchHelper(array, target, startIdx, mid - 1)
    return -1


data = dict(
    array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
    target=33
)

output = binarySearchOptimal(data.get("array"), data["target"])
outPutPrint(data, output)

data = dict(
    array=[0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
    target=0
)

output = binarySearchOptimal(data.get("array"), data["target"])
outPutPrint(data, output)

data = dict(
    array=[1, 5, 23, 111],
    target=35
)

output = binarySearchOptimal(data.get("array"), data["target"])
outPutPrint(data, output)

data = dict(
    array=[1, 5, 23, 111],
    target=111
)

output = binarySearchOptimal(data.get("array"), data["target"])
outPutPrint(data, output)

data = dict(
    array=[5, 23, 111],
    target=3
)

output = binarySearchOptimal(data.get("array"), data["target"])
outPutPrint(data, output)
