def majorityElement(array):
    # Write your code here.
    answer = 0
    for currentBit in range(32):
        currentbitvalue = 1 << currentBit
        onescount = 0

        for num in array:
            if (num & currentbitvalue) != 0:
                onescount += 1

        if onescount > (len(array) / 2):
            answer += currentbitvalue

    return answer


# def majorityElement(array):
#     # Write your code here.
#     answer = array[0]
#     count = 0
#     for i in array:
#         if count == 0:
#             answer = i
#         if i == answer:
#             count += 1
#         else:
#             count -= 1
#
#     return answer
#     return -1


array = [1, 2, 3, 2, 2, 1, 2]
print(f"input nums: {array} \n output nums: {majorityElement(array)}\n")

array = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1]
print(f"input nums: {array} \n output nums: {majorityElement(array)}\n")

array = [1, 2, 3, 2, 2, 1, 2]
print(f"input nums: {array} \n output nums: {majorityElement(array)}\n")

array = [1, 2, 1]
print(f"input nums: {array} \n output nums: {majorityElement(array)}\n")
