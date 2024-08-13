from lib.outPutPrint import outPutPrint


def validIPAddresses(string):
    # Write your code here.
    possible_ips = []

    for i in range(1, min(len(string), 4)):
        current_ip = [""] * 4
        current_ip[0] = string[:i]
        if not isValidIPString(current_ip[0]):
            continue

        for j in range(1 + i, i + min(len(string) - i, 4)):
            current_ip[1] = string[i:j]
            if not isValidIPString(current_ip[1]):
                continue

            for k in range(1 + j, j + min(len(string) - j, 4)):
                current_ip[2] = string[j:k]
                current_ip[3] = string[k:]
                if isValidIPString(current_ip[2]) and isValidIPString(current_ip[3]):
                    possible_ips.append(".".join(current_ip))

    return possible_ips


def isValidIPString(string):
    string_int = int(string)
    if string_int > 255:
        return False
    return len(string) == len(str(string_int))


data = "1921680"
output = validIPAddresses(data)

outPutPrint(data, output)
