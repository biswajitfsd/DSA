def isPalindrome(string):
    # Write your code here.
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True


print(isPalindrome("abcdcba"))
print(isPalindrome("abcdcbad"))
