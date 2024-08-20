from lib.outPutPrint import outPutPrint


def patternMatcher(pattern, string):
    len_string = len(string)
    if len(pattern) > len_string:
        return []
    pattern_arr = get_new_patten(pattern)
    pattern_changed = (pattern_arr[0] != pattern[0])
    first_y, hash_pattern = get_counts_and_first_y(pattern_arr)
    len_x = 1

    return get_match(len_x, first_y, len_string, hash_pattern, pattern_arr, string, pattern_changed)


def get_match(len_x, first_y, len_string, hash_pattern, pattern_arr, string, pattern_changed):
    x = string[0:len_x]
    y = ""
    if "y" in hash_pattern.keys():
        len_y = (len_string - hash_pattern["x"] * len_x) // hash_pattern["y"]
        y_idx = first_y * len_x
        y = string[y_idx:y_idx + len_y]
    pattern_arr_test = list(map(lambda i: x if i == "x" else y, pattern_arr))
    # pattern_arr_test = pattern_arr[:]
    # for i in range(len(pattern_arr_test)):
    #     if pattern_arr_test[i] == "x":
    #         pattern_arr_test[i] = x
    #     else:
    #         pattern_arr_test[i] = y

    if "".join(pattern_arr_test) != string:
        if len_x == len_string:
            return []
        return get_match(len_x + 1, first_y, len_string, hash_pattern, pattern_arr, string, pattern_changed)
    else:
        if pattern_changed:
            return [y, x]
        return [x, y]


def get_new_patten(pattern):
    arr = list(pattern)
    if arr[0] == "x":
        return arr
    else:
        arr = list(map(lambda i: "x" if i == "y" else "y", arr))
        # for i in range(len(arr)):
        #     if arr[i] == "x":
        #         arr[i] = "y"
        #     else:
        #         arr[i] = "x"
    return arr


def get_counts_and_first_y(pattern_array):
    hash_pattern = {}
    first_y = -1
    for i in range(len(pattern_array)):
        if pattern_array[i] in hash_pattern.keys():
            hash_pattern[pattern_array[i]] = hash_pattern[pattern_array[i]] + 1
        else:
            if pattern_array[i] == "y":
                first_y = i
            hash_pattern[pattern_array[i]] = 1

    return first_y, hash_pattern


if __name__ == '__main__':
    data = dict(
        pattern='xxyxxy',
        string='gogopowerrangergogopowerranger'
    )
    output = patternMatcher(data['pattern'], data['string'])

    outPutPrint(data, output)

    data = dict(
        pattern='xxxx',
        string='testtesttesttest'
    )
    output = patternMatcher(data['pattern'], data['string'])

    outPutPrint(data, output)

    data = dict(
        pattern='xxyxyy',
        string='testtestwrongtestwrongtest'
    )
    output = patternMatcher(data['pattern'], data['string'])

    outPutPrint(data, output)

    data = dict(
        pattern='xyx',
        string='thisshouldobviouslybewrong'
    )
    output = patternMatcher(data['pattern'], data['string'])

    outPutPrint(data, output)

    data = dict(
        pattern='yxyx',
        string='abab'
    )
    output = patternMatcher(data['pattern'], data['string'])

    outPutPrint(data, output)
