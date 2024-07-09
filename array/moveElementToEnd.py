def moveElementToEnd(array, toMove):
    # Write your code here.
    to_move_array = []
    not_to_move_array = []
    for i in range(len(array)):
        if array[i] == toMove:
            not_to_move_array.append(array[i])
        else:
            to_move_array.append(array[i])

    return to_move_array + not_to_move_array
    pass


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove))
