def sweetAndSavory(dishes, target):
    sweet = sorted([dish for dish in dishes if dish < 0], key=abs)
    savory = sorted([dish for dish in dishes if dish > 0])
    best_pair = [0] * 2
    best_diff = float('inf')
    sweet_index, savory_index = 0, 0

    while sweet_index < len(sweet) and savory_index < len(savory):
        current_sum = sweet[sweet_index] + savory[savory_index]

        if current_sum <= target:
            current_diff = target - current_sum
            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [sweet[sweet_index], savory[savory_index]]
            savory_index += 1
        else:
            sweet_index += 1

    return best_pair


# array = [-3, -5, 1, 7]
# target = 8
# print(f"input array: {array}, target: {target} \n output nums: {sweetAndSavory(array, target)}\n")

# array = [2, 5, -4, -7, 12, 100, -25]
# target = -20
# print(f"input array: {array}, target: {target} \n output nums: {sweetAndSavory(array, target)}\n")

array = [-12, 13, 100, -53, 540, -538, 53, 76, 32, -63]
target = -15
print(f"input array: {array}, target: {target} \n output nums: {sweetAndSavory(array, target)}\n")
