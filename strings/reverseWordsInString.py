from lib.outPutPrint import outPutPrint


def reverseWordsInString_First(string):
    reversed_str = ""
    current_phase = ""
    str_len = len(string)
    for i in range(str_len):
        if string[i] != ' ':
            current_phase += string[i]
        elif string[i] == ' ' and string[i - 1] != ' ':
            reversed_str = string[i] + current_phase + reversed_str
            current_phase = ""
        elif string[i] == ' ' and string[i - 1] == ' ':
            reversed_str = string[i] + reversed_str
        else:
            reversed_str = string[i] + reversed_str
    reversed_str = current_phase + reversed_str
    return reversed_str


def reverseWordsInString_second(string):
    reversed_str = []
    str_len = len(string)
    start_index = 0
    for i in range(str_len):
        if string[i] == ' ':
            reversed_str.append(string[start_index:i])
            start_index = i
        elif string[start_index] == ' ':
            reversed_str.append(" ")
            start_index = i

    reversed_str.append(string[start_index:])
    reverseList(reversed_str)
    return "".join(reversed_str)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


def reverseWordsInString(string):
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)
    start_idx = 0
    while start_idx < len(characters):
        end_idx = start_idx
        while end_idx < len(characters) and characters[end_idx] != ' ':
            end_idx += 1

        reverseListRange(characters, start_idx, end_idx - 1)
        start_idx = end_idx + 1

    return "".join(characters)


def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


data = "AlgoExpert is the best!"
# data = "test        "
# expe = "        test"
# output = reverseWordsInString_second(data)
output = reverseWordsInString(data)

outPutPrint(data, output)
