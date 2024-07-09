def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    last_element = sorted_intervals[-1]
    return overlappingIntervals(0, 2, sorted_intervals, last_element)


def overlappingIntervals(i, j, input, last_element):
    first_element = input[i:j]
    rest_elements = input[j:]
    if (first_element[0][0] <= first_element[1][0] <= first_element[0][1]) or (
            first_element[0][0] <= first_element[1][1] <= first_element[0][1]):
        ot = sorted([first_element[0][0], first_element[0][1], first_element[1][0], first_element[1][1]])
        ot = [ot[0], ot[-1]]
        if i > 0:
            input = input[:i] + [ot] + rest_elements
        else:
            input = [ot] + rest_elements
        if first_element[1] is last_element:
            return input
        return overlappingIntervals(i, j, input, last_element)
    else:
        if i > 0:
            input = input[:i] + first_element + rest_elements
        else:
            input = first_element + rest_elements
        i += 1
        j += 1
    if first_element[1] is last_element:
        return input
    return overlappingIntervals(i, j, input, last_element)


# intervals = [
#     [1, 2],
#     [6, 8],
#     [4, 7],
#     [3, 5],
#     [9, 10]
# ]
# intervals = [
#     [1, 10],
#     [10, 20],
#     [20, 30],
#     [30, 40],
#     [40, 50],
#     [50, 60],
#     [60, 70],
#     [70, 80],
#     [80, 90],
#     [90, 100]
# ]
# intervals = [
#     [1, 22],
#     [-20, 30]
# ]
intervals = [
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
]
print(mergeOverlappingIntervals(intervals))


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            del intervals[i + 1]
        else:
            i += 1

    return intervals
