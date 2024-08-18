from lib.outPutPrint import outPutPrint


def underscorifySubstring(string, substring):
    array_of_substrings = []
    current_idx = 0
    len_substring = len(substring)
    while current_idx < len(string):
        idx = find_substring(string, substring, current_idx)
        if idx == -1:
            break
        array_of_substrings.append([idx, idx + len_substring])
        current_idx = idx + 1

    array_of_substrings = collapseLocations(array_of_substrings)
    print(array_of_substrings)
    return underScoreSubstring(string, array_of_substrings)


def find_substring(string, substring, idx):
    return string.find(substring, idx)


def collapseLocations(list_of_substrings):
    if not list_of_substrings:
        return list_of_substrings
    collapsed_substrings_array = [list_of_substrings[0]]
    current_idx_for_collapse = 0
    for i in range(len(list_of_substrings)):
        collapsed_substrings_last_idx = collapsed_substrings_array[current_idx_for_collapse][1]
        if collapsed_substrings_last_idx >= list_of_substrings[i][0]:
            collapsed_substrings_array[current_idx_for_collapse][1] = list_of_substrings[i][1]
        else:
            collapsed_substrings_array.append(list_of_substrings[i])
            current_idx_for_collapse = current_idx_for_collapse + 1

    return collapsed_substrings_array


def underScoreSubstring(string, array_of_substrings):
    string_array = list(string)
    for i in range(len(array_of_substrings)):
        string_array[array_of_substrings[i][0]] = "_" + string_array[array_of_substrings[i][0]]
        string_array[array_of_substrings[i][1] - 1] = string_array[array_of_substrings[i][1] - 1] + "_"

    return "".join(string_array)


data = dict(
    string='testthis is a testtest to see if testestest it works',
    substring='test',
)
output = underscorifySubstring(data['string'], data['substring'])

outPutPrint(data, output)
