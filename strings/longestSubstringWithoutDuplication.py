from lib.outPutPrint import outPutPrint


def longestSubstringWithoutDuplication(string):
    hash_sting = {}
    start_index = 0
    current_longest = ""
    for i in range(len(string)):
        if string[i] not in hash_sting:
            if len(string[start_index:i + 1]) > len(current_longest):
                current_longest = string[start_index:i + 1]
            hash_sting[string[i]] = i
        else:
            start_index = max(start_index, hash_sting[string[i]] + 1)
            if len(string[start_index:i + 1]) > len(current_longest):
                current_longest = string[start_index:i + 1]
            hash_sting[string[i]] = i

    return current_longest


data = "clementisacap"
output = longestSubstringWithoutDuplication(data)

outPutPrint(data, output)
