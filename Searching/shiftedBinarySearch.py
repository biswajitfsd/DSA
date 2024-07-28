from lib.outPutPrint import outPutPrint


def shiftedBinarySearch(array, target):
    startIdx, endIdx = 0, len(array) - 1
    while startIdx <= endIdx:
        mid = (startIdx + endIdx) // 2
        mid_val = array[mid]
        start_val = array[startIdx]
        end_vel = array[endIdx]
        if mid_val == target:
            return mid
        elif start_val <= mid_val:
            if mid_val > target >= start_val:
                endIdx = mid - 1
            else:
                startIdx = mid + 1
        else:
            if mid_val < target <= end_vel:
                startIdx = mid + 1
            else:
                endIdx = mid - 1
    return -1


def shiftedBinarySearch_v2(array, target):
    startIdx, endIdx = 0, len(array) - 1
    return shiftedBinarySearchHelper(array, target, startIdx, endIdx)


def shiftedBinarySearchHelper(array, target, startIdx, endIdx):
    if startIdx > endIdx:
        return -1
    mid = (startIdx + endIdx) // 2
    mid_val = array[mid]
    start_val = array[startIdx]
    end_vel = array[endIdx]
    if mid_val == target:
        return mid
    elif start_val <= mid_val:
        if mid_val > target >= start_val:
            return shiftedBinarySearchHelper(array, target, startIdx, mid - 1)
        else:
            return shiftedBinarySearchHelper(array, target, mid + 1, endIdx)
    else:
        if mid_val < target <= end_vel:
            return shiftedBinarySearchHelper(array, target, mid + 1, endIdx)
        else:
            return shiftedBinarySearchHelper(array, target, startIdx, mid - 1)


data = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
output = shiftedBinarySearch(data, target)

outPutPrint(data, output)

data = [111, 1, 5, 23]
target = 5
output = shiftedBinarySearch(data, target)

outPutPrint(data, output)

data = [5, 23, 111, 1]
target = 111
output = shiftedBinarySearch(data, target)

outPutPrint(data, output)

data = [72, 73, 0, 1, 21, 33, 37, 45, 61, 71]
target = 72
output = shiftedBinarySearch(data, target)

outPutPrint(data, output)
