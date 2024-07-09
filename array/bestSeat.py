# def bestSeat(seats):
#     max_length, max_length_index = logestSeqOfZero(seats)
#     print(max_length, max_length_index, "\n")
#     if max_length == 1:
#         return max_length_index
#     elif max_length > 1:
#         if max_length % 2 == 0:
#             result = max_length_index + ((max_length // 2) - 1)
#         else:
#             result = max_length_index + (max_length // 2)
#         return result
#     return -1
#
#
# def logestSeqOfZero(seats):
#     current_sequence_length = 0
#     current_sequence_index = -1
#     max_length = 0
#     max_length_index = -1
#
#     for i in range(0, len(seats) - 1):
#         if seats[i] == 0:
#             if current_sequence_length == 0:
#                 current_sequence_index = i
#             current_sequence_length += 1
#             if current_sequence_length > max_length:
#                 max_length = current_sequence_length
#                 max_length_index = current_sequence_index
#         else:
#             current_sequence_length = 0
#
#     return max_length, max_length_index


def bestSeat(seats):
    best = -1
    zero = start = length = 0
    for i, num in enumerate(seats):
        if num == 0:
            zero += 1
        else:
            if zero > length:
                best, length = (i + start) // 2, zero
            zero, start = 0, i
    return best


seats = [1, 0, 1, 0, 0, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 0, 0, 1, 0, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 1, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 0, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
seats = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
print(f"Output for {seats}: ", bestSeat(seats), "\n")
