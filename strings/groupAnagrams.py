from lib.outPutPrint import outPutPrint


def groupAnagrams_first(words):
    # Write your code here.
    words_ordered = ["".join(sorted(list(i))) for i in words]
    set_visited = dict()
    for i, word in enumerate(words_ordered):
        if word not in set_visited:
            set_visited[word] = [i]
        else:
            set_visited[word].append(i)

    result = [0] * len(set_visited)
    for j, value in enumerate(set_visited):
        vals = set_visited[value]
        result[j] = [0] * len(vals)
        for k, val in enumerate(vals):
            result[j][k] = words[val]

    return result

def groupAnagrams(words):
    # Write your code here.
    set_visited = {}
    for word in words:
        sorted_word = "".join(sorted(list(word)))
        if sorted_word not in set_visited:
            set_visited[sorted_word] = [word]
        else:
            set_visited[sorted_word].append(word)
    return list(set_visited.values())


data = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
output = groupAnagrams(data)

outPutPrint(data, output)
