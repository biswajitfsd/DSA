def isMonotonic(array):
    i = 0
    j = len(array) - 1
    lesser = 0
    greater = 0
    same = 0
    while i < j:
        if array[i] < array[i + 1]:
            lesser = lesser + 1
        elif array[i] > array[i + 1]:
            greater = greater + 1
        else:
            same = same + 1

        if lesser > 0 and greater > 0:
            return False

        i += 1

    if (lesser > 0 and greater == 0) or (greater > 0 and lesser == 0) or (
            lesser == 0 and greater == 0 and same == 0) or (lesser == 0 and greater == 0 and same > 0) or (
            lesser > 0 and greater == 0 and same > 0) or (lesser == 0 and greater > 0 and same > 0):
        return True


pass

# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
array = [1, 1, 1, 2, 3, 4, 1]
print(isMonotonic(array))
