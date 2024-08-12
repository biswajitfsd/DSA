from lib.outPutPrint import outPutPrint


def getLongestPalindromicSubstring(s, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(s):
        if s[left_idx] != s[right_idx]:
            break
        left_idx -= 1
        right_idx += 1

    return [left_idx + 1, right_idx]


def longestPalindromicSubstring(string):
    current_palindromic = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromicSubstring(string, i - 1, i + 1)
        even = getLongestPalindromicSubstring(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_palindromic = max(longest, current_palindromic, key=lambda x: x[1] - x[0])

    return string[current_palindromic[0]:current_palindromic[1]]


data = "abaxyzzyxf"
output = longestPalindromicSubstring(data)

outPutPrint(data, output)
