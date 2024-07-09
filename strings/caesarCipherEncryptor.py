# def caesarCipherEncryptor(string, key):
#     # Write your code here.
#     if key == 0:
#         return string
#     start = ord("a")
#     end = ord("z")
#     str_len = len(string)
#     final_string = last_later = string[-1]
#     last_later_ascii = ord(last_later)
#     i = 0
#     while i < key:
#         if last_later_ascii == end:
#             last_later_ascii = start
#         else:
#             last_later_ascii = last_later_ascii + 1
#         final_string += chr(last_later_ascii)
#         if len(final_string) > str_len:
#             final_string = final_string[1:]
#         i += 1
#     return final_string

def caesarCipherEncryptor(string, key):
    start = ord("a")
    end = ord("z")
    if key > 26:
        key = key % 26
    if key == 0:
        return string
    result = ""
    for i in range(0, len(string)):
        char = ord(string[i]) + key
        if char > end:
            char = start + (char - end - 1)
        result += (chr(char))
    return result


input = dict(
    string="xyz",
    key=5
)

output = caesarCipherEncryptor(input["string"], input["key"])
print(f"input: {input} \n output: {output}")

input = dict(
    string="ovmqkwtujqmfkao",
    key=52
)

output = caesarCipherEncryptor(input["string"], input["key"])
print(f"input: {input} \n output: {output}")
