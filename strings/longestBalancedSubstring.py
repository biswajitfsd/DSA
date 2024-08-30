from lib.outPutPrint import outPutPrint


# O(n) Time | O(1) space
def longestBalancedSubstring(string):
    longest_length = 0
    opening_count = 0
    closing_count = 0

    for i in range(len(string)):
        if string[i] == '(':
            opening_count += 1
        else:
            closing_count += 1

        if opening_count == closing_count:
            longest_length = max(opening_count + closing_count, longest_length)
        elif closing_count > opening_count:
            opening_count = 0
            closing_count = 0

    opening_count = 0
    closing_count = 0

    for i in reversed(range(len(string))):
        if string[i] == '(':
            opening_count += 1
        else:
            closing_count += 1

        if opening_count == closing_count:
            longest_length = max(opening_count + closing_count, longest_length)
        elif closing_count < opening_count:
            opening_count = 0
            closing_count = 0

    return longest_length


# O(n) Time | O(n) space
def longestBalancedSubstring_sol_2(string):
    # Write your code here.
    longest_length = 0
    index_stack = [-1]
    for i in range(len(string)):
        if string[i] == '(':
            index_stack.append(i)
        else:
            index_stack.pop()
            if len(index_stack) == 0:
                index_stack.append(i)
            else:
                balanced_sub_string_idx = index_stack[len(index_stack) - 1]
                current_length = i - balanced_sub_string_idx
                longest_length = max(current_length, longest_length)

    return longest_length


# O(n^3) Time | O(n) space
def longestBalancedSubstring_sol_1(string):
    # Write your code here.
    longest_length = 0

    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1, 2):
            if is_balanced_string(string[i:j]):
                longest_length = max(longest_length, j - i)
    return longest_length


def is_balanced_string(string):
    open_parentheses_stack = []
    for char in string:
        if char == "(":
            open_parentheses_stack.append("(")
        elif len(open_parentheses_stack) > 0:
            open_parentheses_stack.pop()
        else:
            return False

    return len(open_parentheses_stack) == 0


data = "(()))("
output = longestBalancedSubstring(data)
outPutPrint(data, output)

data = "())()(()())"
output = longestBalancedSubstring(data)
outPutPrint(data, output)
