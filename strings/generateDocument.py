def generateDocument(characters, document):
    # Write your code here.
    if len(document) == 0:
        return True;
    characters_set = dict()
    for character in characters:
        characters_set[character] = characters_set.get(character, 0) + 1

    document_set = dict()
    for string in document:
        document_set[string] = document_set.get(string, 0) + 1

    status = True
    for data in document_set.keys():
        if data in characters_set:
            if characters_set[data] < document_set[data]:
                return False
        else:
            return False

    return status


input = dict(
    characters="Bste!hetsi ogEAxpelrt x ",
    document="AlgoExpert is the Best!"
)

output = generateDocument(input["characters"], input["document"])
print(f"input: {input} \n output: {output}")

input = dict(
    characters="aheaolabbhb",
    document="hello"
)

output = generateDocument(input["characters"], input["document"])
print(f"input: {input} \n output: {output}")
