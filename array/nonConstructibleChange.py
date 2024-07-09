def nonConstructibleChange(coins):
    # Write your code here.
    sorted_coins = sorted(coins)
    amount_of_change = 0

    for coin in sorted_coins:
        if coin <= amount_of_change + 1:
            amount_of_change += coin
        else:
            return amount_of_change + 1
    return amount_of_change + 1


print(nonConstructibleChange([6, 4, 5, 1, 1, 8, 9]))
# print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
