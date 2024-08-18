from lib.outPutPrint import outPutPrint


# O(n+m)
def oneEdit_first_case(stringOne, stringTwo):
    lenOne, lenTwo = len(stringOne), len(stringTwo)
    if abs(lenOne - lenTwo) > 1:
        return False

    for i in range(min(lenOne, lenTwo)):
        if stringOne[i] != stringTwo[i]:
            if lenOne > lenTwo:
                return stringOne[i + 1:] == stringTwo[i:]
            elif lenTwo > lenOne:
                return stringOne[i:] == stringTwo[i + 1:]
            else:
                return stringTwo[i + 1:] == stringOne[i + 1:]

    return True


def oneEdit(stringOne, stringTwo):
    lenOne, lenTwo = len(stringOne), len(stringTwo)
    if abs(lenOne - lenTwo) > 1:
        return False
    made_edit = False
    indexOne, indexTwo = 0, 0
    while indexOne < lenOne and indexTwo < lenTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if made_edit:
                return False
            made_edit = True

            if lenOne > lenTwo:
                indexOne += 1
            elif lenTwo > lenOne:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1

    return True


data = dict(
    stringOne="bb",
    stringTwo="a",
)
output = oneEdit(data["stringOne"], data["stringTwo"])

outPutPrint(data, output)
