from lib.outPutPrint import outPutPrint

# This will work only for all positive numbers
def findThreeLargestNumbers_v2(array):
    output_arr = [None] * 3
    for i in reversed(range(0, len(output_arr))):
        largest_number = 0
        largest_number_index = 0
        for j in range(0, len(array)):
            if array[j] is None:
                continue
            if array[j] > largest_number:
                largest_number = array[j]
                largest_number_index = j
        output_arr[i] = largest_number
        array[largest_number_index] = None

    return output_arr
def findThreeLargestNumbers(array):
    output_arr = [None, None, None]
    for num in array:
        update_largest(output_arr, num)
    return output_arr


def update_largest(output_arr, num):
    if output_arr[2] is None or num > output_arr[2]:
        shift_and_update(output_arr, num, 2)
    elif output_arr[1] is None or num > output_arr[1]:
        shift_and_update(output_arr, num, 1)
    elif output_arr[0] is None or num > output_arr[0]:
        shift_and_update(output_arr, num, 0)


def shift_and_update(output_arr, num, idx):
    for i in range(idx + 1):
        if i == idx:
            output_arr[i] = num
        else:
            output_arr[i] = output_arr[i + 1]


data = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
output = findThreeLargestNumbers(data)

outPutPrint(data, output)
