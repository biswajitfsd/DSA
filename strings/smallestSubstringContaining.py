from lib.outPutPrint import outPutPrint


# Slide Window technique
# O(B+S) T/S
def smallestSubstringContaining(bigString, smallString):
    small_string_set = sendStringSetSorted(smallString)
    subs_string_bounds = get_substring_bound(bigString, small_string_set)
    print(subs_string_bounds)
    return get_string_from_bound(bigString, subs_string_bounds)


def sendStringSetSorted(string):
    string_set = {}
    for char in string:
        increment_set_key_count(char, string_set)
    return string_set


def increment_set_key_count(char, string_set):
    if char not in string_set:
        string_set[char] = 0
    string_set[char] += 1


def decrement_set_key_count(char, string_set):
    string_set[char] -= 1


def get_substring_bound(bigString, small_string_set):
    characters_found_set = {}
    no_of_unique_chars = len(small_string_set.keys())
    characters_found = 0
    left_idx = 0
    right_idx = 0
    smallest_substring_bound = [0, float("inf")]
    while right_idx < len(bigString):
        right_char = bigString[right_idx]
        if right_char not in small_string_set:
            right_idx += 1
            continue

        increment_set_key_count(right_char, characters_found_set)

        if characters_found_set[right_char] == small_string_set[right_char]:
            characters_found += 1

        while characters_found == no_of_unique_chars and left_idx <= right_idx:
            smallest_substring_bound = get_closer_substring_bound(left_idx, right_idx, smallest_substring_bound[0],
                                                                  smallest_substring_bound[1])
            left_char = bigString[left_idx]
            if left_char not in small_string_set:
                left_idx += 1
                continue
            if characters_found_set[left_char] == small_string_set[left_char]:
                characters_found -= 1
            decrement_set_key_count(left_char, characters_found_set)
            left_idx += 1

        right_idx += 1

    return smallest_substring_bound


def get_closer_substring_bound(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]


def get_string_from_bound(bigString, subs_string_bounds):
    start, end = subs_string_bounds
    if end == float("inf"):
        return ""
    return bigString[start:end + 1]


data = {
    "bigString": "abcd$ef$axb$c$",
    "smallString": "$$abf"
}
output = smallestSubstringContaining(data["bigString"], data["smallString"])

outPutPrint(data, output)
