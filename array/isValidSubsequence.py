# def isValidSubsequence(array, sequence):
#     sequence_len = len(sequence)
#     i = 0  # pointer for sequence
#     j = 0  # pointer for array
#
#     while i < sequence_len and j < len(array):
#         if sequence[i] == array[j]:
#             i += 1  # move to next element in sequence
#         j += 1  # move to next element in array (regardless of match)
#
#     # If we reach the end of the sequence, all elements were found in the correct order
#     return i == sequence_len
def isValidSubsequence(array, sequence):
    sequence_len = len(sequence)
    array_len = len(array)
    sequence_index_in_array = []

    if sequence_len > array_len:
        return False

    for num in sequence:
        if num not in array:
            return False
        else:
            seq_ind = array.index(num)
            sequence_index_in_array.append(seq_ind)
            array[seq_ind] = None

    sequence_index_in_array_sort = sorted(sequence_index_in_array)
    if sequence_index_in_array_sort != sequence_index_in_array:
        return False

    return True
    pass


# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [5, 1, 25, 22, 6, -1, 8, 10]

# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [5, 1, 22, 22, 6, -1, 8, 10]

array = [1, 1, 1, 1, 1]
sequence = [1, 1, 1]

print("Status: ", isValidSubsequence(array, sequence))
