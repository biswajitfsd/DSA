def longestPeak(array):
    # Write your code here.
    isIncreasing = False
    isDecreasing = False
    currentPeak, maxPeak = 0, 0
    for i in range(1, len(array)):
        p_num = array[i - 1]
        c_num = array[i]

        if c_num > p_num:
            isIncreasing = True
            if isDecreasing is False:
                if currentPeak == 0:
                    currentPeak += 2
                else:
                    currentPeak += 1
            else:
                maxPeak = max(maxPeak, currentPeak)
                currentPeak = 2
        elif c_num < p_num:
            if currentPeak == 0:
                isIncreasing, isDecreasing = False, False
                continue
            else:
                currentPeak += 1
                isIncreasing, isDecreasing = False, True

        else:
            if isDecreasing is True:
                maxPeak = max(maxPeak, currentPeak)

            currentPeak = 0
            isIncreasing, isDecreasing = False, False

    if isDecreasing is True:
        return max(currentPeak, maxPeak)
    return maxPeak
    pass


# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
print(longestPeak(array))
