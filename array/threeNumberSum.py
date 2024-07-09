def threeNumberSum(array, targetSum):
    # Write your code here.
    sorted_array = sorted(array)
    result_array = []
    print("Input: ", sorted_array)
    i = 0
    length = len(sorted_array)
    while i < length:
        j = i + 1
        while j < length:
            if sorted_array[i] + sorted_array[i - 1] + sorted_array[j] == targetSum:
                result_array.append([sorted_array[i], sorted_array[i - 1], sorted_array[j]])
            j += 1
            if j == length:
                i += 1

        if i == length:
            i += 1
    #
    # for i in range(len(sorted_array)):
    #     for j in range(len(sorted_array)):
    #         print([sorted_array[i], sorted_array[i - 1], sorted_array[j]])
    #         if targetSum == sorted_array[i - 1] + sorted_array[i] + sorted_array[j]:
    #             result_array.append([sorted_array[i], sorted_array[i - 1], sorted_array[j]])

    return result_array
    pass


array = [12, 3, 1, 2, -6, 5, -8, 6]
print("output: ", threeNumberSum(array=array, targetSum=0))
