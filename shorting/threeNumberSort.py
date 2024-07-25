from time import time_ns

from lib.outPutPrint import outPutPrint


def threeNumberSort(array, order):
    n = len(array)
    last_index_updated = 0
    for i in order:
        if i not in array:
            continue
        j = last_index_updated
        while j < n:
        # for j in range(last_index_updated, n):
            if array[j] == i:
                array[last_index_updated], array[j] = array[j], array[last_index_updated]
                last_index_updated += 1
            j += 1
    return array


data = dict(
    array=[1, 0, 0, -1, -1, 0, 1, 1],
    order=[0, 1, -1]
)
start_time = time_ns()
output = threeNumberSort(data.get("array"), data.get("order"))
print(time_ns() - start_time)

outPutPrint(data, output)
