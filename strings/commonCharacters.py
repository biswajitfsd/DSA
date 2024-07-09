def commonCharacters(strings):
    # Write your code here.
    all_string = set()
    length = len(strings)
    result = []
    for string in strings:
        crr_set = set(string)
        all_string = all_string | crr_set
    arr = list(all_string)
    for i in range(len(arr)):
        count = 0
        for string in strings:
            if arr[i] in string:
                count += 1

        if count == length:
            result.append(arr[i])
    return result


#
# def commonCharacters(strings):
#     # Write your code here.
#     all_string = dict()
#     length = len(strings)
#     result = []
#     for string in strings:
#         for char in string:
#             all_string[char] = all_string.get(char, 0) + 1
#
#     for char in all_string:
#         if all_string[char] % length == 0:
#             result.append(char)
#     return result


# input = dict(
#     string=["abc", "bcd", "cbad"]
# )
#
# output = commonCharacters(input["string"])
# print(f"input: {input} \n output: {output}")
# def commonCharacters(strings):
#     return list(set.intersection(*map(set, strings)))


input = dict(
    string=["aa", "aa"]
)

output = commonCharacters(input["string"])
print(f"input: {input} \n output: {output}")
