from lib.outPutPrint import outPutPrint


def searchForRange(array, target):
    start_idx = 0
    end_idx = len(array) - 1
    result = [-1, -1]
    range_start_idx = range_end_idx = binarySearchHelper(array, target, start_idx, end_idx)
    print(range_start_idx)
    while range_end_idx <= end_idx and array[range_end_idx] == target:
        result = [range_start_idx, range_end_idx]
        range_end_idx += 1

    return result


def binarySearchHelper(array, target, startIdx, endIdx):
    while startIdx <= endIdx:
        mid = (startIdx + endIdx) // 2
        if array[mid] == target:
            if array[mid] == array[mid - 1]:
                endIdx = mid - 1
            else:
                return mid
        if target > array[mid]:
            startIdx = mid + 1
        if target < array[mid]:
            endIdx = mid - 1
    return -1


data = dict(
    array=[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73],
    target=45
)

output = searchForRange(data.get("array"), data["target"])
outPutPrint(data, output)

data = dict(
    array=[5, 7, 7, 8, 8, 10],
    target=10
)

output = searchForRange(data.get("array"), data["target"])
outPutPrint(data, output)
