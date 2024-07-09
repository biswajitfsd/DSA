def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    sortedArrayOne = sorted(arrayOne)
    sortedArrayTwo = sorted(arrayTwo)
    i = 0
    j = 0
    smallest_diff = 0
    result = [0] * 2
    while i < len(sortedArrayOne) and j < len(sortedArrayTwo):
        one = sortedArrayOne[i]
        two = sortedArrayTwo[j]
        if abs(one - two) == smallest_diff:
            result[0] = one
            result[1] = two
            return result
        else:
            if i == len(sortedArrayOne) - 1 and j == len(sortedArrayTwo) - 1:
                smallest_diff += 1
                j = 0
                i = 0
            else:
                if j == len(sortedArrayTwo) - 1:
                    i += 1
                    j = 0
                else:
                    j += 1
    pass


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))
