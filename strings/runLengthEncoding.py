from lib.outPutPrint import outPutPrint


def runLengthEncoding(string):
    # Write your code here.
    max_num = 9
    curernt_char = string[0]
    curernt_num = 0
    output = ''
    for char in string:
        if char == curernt_char:
            if curernt_num < max_num:
                curernt_num = curernt_num + 1
            else:
                output = f"{output}{str(curernt_num)}{curernt_char}"
                curernt_num = 1
        else:
            output = f"{output}{str(curernt_num)}{curernt_char}"
            curernt_char = char
            curernt_num = 1
    output = f"{output}{str(curernt_num)}{curernt_char}"
    return output


input = dict(
    string="AAAAAAAAAAAAABBCCCCDD"
)

output = runLengthEncoding(input["string"])
outPutPrint(input, output)
