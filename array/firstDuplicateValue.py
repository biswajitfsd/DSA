# def firstDuplicateValue(array):
#     # Write your code here.
#     i = 0
#     j = len(array) - 1
#     seen = set()
#     duplicate_val = dict()
#     while i < j:
#         if array[i] == array[j]:
#             if array[i] in seen:
#                 if duplicate_val[array[i]] > j:
#                     duplicate_val[array[i]] = j
#             else:
#                 duplicate_val[array[i]] = j
#                 seen.add(array[i])
#
#             j -= 1
#         else:
#             j -= 1
#
#         if i == j:
#             i += 1
#             j = len(array) - 1
#
#     if len(duplicate_val) > 0:
#         print(duplicate_val)
#         key_of_min_value = min(duplicate_val, key=duplicate_val.get)
#         return key_of_min_value
#     return -1


def firstDuplicateValue(array):
    # Write your code here.
    s = set()
    for i in array:
        if i in s:
            return i
        else:
            s.add(i)

    return -1


# array = [2, 1, 5, 2, 3, 3, 4]
# array = [2, 1, 5, 3, 3, 2, 4]
array = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]
# array = [23, 21, 22, 5, 3, 13, 11, 16, 5, 11, 9, 14, 23, 3, 2, 2, 5, 11, 6, 11, 23, 8, 1]
print(firstDuplicateValue(array))
