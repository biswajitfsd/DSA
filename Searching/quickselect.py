from lib.outPutPrint import outPutPrint


def quickselect(array, k):
    position = k - 1
    return quickselectHelper(array, 0, len(array) - 1, position)


def quickselectHelper(array, startIdx, endIdx, position):
    while True:
        pivot = startIdx
        left = startIdx + 1
        rightIdx = endIdx
        while left <= rightIdx:
            if array[left] > array[pivot] > array[rightIdx]:
                array[left], array[rightIdx] = array[rightIdx], array[left]
            if array[left] <= array[pivot]:
                left += 1
            if array[rightIdx] >= array[pivot]:
                rightIdx -= 1
        array[pivot], array[rightIdx] = array[rightIdx], array[pivot]
        if rightIdx == position:
            return array[position]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def quickselect_v2(array, k):
    n = len(array)
    for i in range(0, k):
        smallest_index = i
        for j in range(i + 1, n):
            if array[j] < array[smallest_index]:
                smallest_index = j

        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array[k - 1]


data = dict(
    array=[8, 5, 2, 9, 7, 6, 3],
    target=3
)

output = quickselect(data.get("array"), data["target"])
outPutPrint(data, output)
