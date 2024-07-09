# def fourNumberSum(array, targetSum):
#     # Write your code here.
#     pair_array = []
#     result_pair = []
#     i = 0
#     while i < len(array):
#         pair_array.append(array[i:i + 2])
#         i += 2
#
#     for i in range(len(pair_array)):
#         for j in range(i + 1, len(pair_array)):
#             if sum(pair_array[i]) + sum(pair_array[j]) == targetSum:
#                 result_pair_arr = pair_array[i] + pair_array[j]
#                 if len(result_pair_arr) == 4:
#                     result_pair.append(result_pair_arr)
#
#     return result_pair


def fourNumberSum(array, targetSum):
    result = []
    hash = dict()
    for i in range(len(array)):
        a1 = array[:i+1]
        a2 = array[i+1:]
        for a in a2:
            sum = array[i] + a
            sum = targetSum - sum
            hash_found = hash.get(sum, 0)
            if hash_found != 0:
                for each in hash_found:
                    result.append(each+[array[i], a])
        for k, each in enumerate(a1):
            if k != i:
                sum = array[i] + each
                if sum not in hash:
                    hash[sum] = [[each, array[i]]]
                else:
                    hash[sum].append([each, array[i]])

    return result


# array = [7, 6, 4, -1, 1, 2]
# targetSum = 16
array = [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
targetSum = 4
# array = [1, 2, 3, 4, 5, 6, 7]
# targetSum = 10

print(fourNumberSum(array, targetSum))
