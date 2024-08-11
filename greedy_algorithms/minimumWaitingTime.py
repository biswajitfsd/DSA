from lib.outPutPrint import outPutPrint


def minimumWaitingTime_n2(queries):
    int_value = 0
    i = 1
    while i < len(queries):
        int_value += sum(queries[0:i])
        i += 1

    return int_value


def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    current_waiting_time = 0
    for i in range(1, len(queries)):
        current_waiting_time += queries[i - 1]
        total_waiting_time += current_waiting_time

    return total_waiting_time


# data = [3, 2, 1, 2, 6]
data = [1, 2, 2, 3, 6]
# print(0 + (0 + 1) + (0 + 1 + 2) + (0 + 1 + 2 + 2) + (0 + 1 + 2 + 2 + 3))
output = minimumWaitingTime(data)
outPutPrint(data, output)
