from lib.outPutPrint import outPutPrint


def firstNonRepeatingCharacter(string):
    visited = set()
    for i in range(len(string)):
        try:
            string.index(string[i], i + 1)
            if string[i] not in visited:
                visited.add(string[i])
        except ValueError:
            if string[i] not in visited:
                return i
    return -1


# given_input = dict(
#     string="abcdcaf"
# )
# output = firstNonRepeatingCharacter(given_input["string"])
# outPutPrint(given_input, output)

given_input = dict(
    string="faadabcbbebdf"
)
output = firstNonRepeatingCharacter(given_input["string"])
outPutPrint(given_input, output)
