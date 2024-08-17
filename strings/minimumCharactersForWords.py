from lib.outPutPrint import outPutPrint

# Time Complexity:
# O(n⋅m), where n is the number of words, and m is the average length of the words. This is because the algorithm must process each character in each word multiple times.
# Space Complexity:
# O(n⋅m+k), where k is the number of distinct characters, and n \cdot m accounts for the worst-case scenario where all characters must be stored in the result list.
def minimumCharactersForWords(words):
    result = []
    main_word_hash = {}
    for word in words:
        word_hash = {}
        for letter in word:
            if letter not in word_hash:
                word_hash[letter] = 1
            else:
                word_hash[letter] += 1
        for letter in word_hash:
            if letter in main_word_hash and main_word_hash[letter] < word_hash[letter]:
                main_word_hash[letter] = word_hash[letter]
            elif letter not in main_word_hash:
                main_word_hash[letter] = word_hash[letter]

    for letter in main_word_hash:
        for i in range(main_word_hash[letter]):
            result.append(letter)
    return result

data = ["this", "that", "did", "deed", "them!", "a"]
output = minimumCharactersForWords(data)

outPutPrint(data, output)
