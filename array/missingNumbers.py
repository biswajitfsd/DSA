def missingNumbers(nums):
    # Write your code here.
    array = list(range(1, len(nums) + 3))
    diff = sorted(list(set(array) - set(nums)))

    return diff


nums = [1, 4, 3]
print(missingNumbers(nums))
