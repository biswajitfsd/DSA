def zeroSumSubarray(nums):
    # Write your code here.
    sums = set([0])
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in sums:
            return True
        sums.add(current_sum)

    return False


nums = [-5, -5, 2, 3, -2]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = []
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = [0]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = [1, 2, 3]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = [-2, -3, -1, 2, 3, 4, -5, -3, 1, 2]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = [1, 2, -2, 3]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
nums = [2, 3, 4, -5, -3, 5, 5]
print(f"input nums: {nums} \n output nums: {zeroSumSubarray(nums)}\n")
