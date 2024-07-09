from lib.outPutPrint import outPutPrint


# def semordnilap(words):
#     # Write your code here.
#     already_passed = set()
#     result = []
#     for i in range(len(words)):
#         word = words[i]
#         if word not in already_passed:
#             reversed_word = word[::-1]
#             already_passed.add(word)
#             in_words = False
#             try:
#                 if words.index(reversed_word, i + 1):
#                     in_words = True
#             except ValueError:
#                 in_words = False
#             if in_words:
#                 already_passed.add(reversed_word)
#                 result.append([word, reversed_word])
#
#     return result
def semordnilap(words):
    seen_words = set([])
    result = []
    for original in words:
        flipped = original[::-1]
        # If we have seen the flipped version then
        # we must have a pair. Add the pair to the result.
        if flipped in seen_words:
            result.append([ original, flipped ])
        seen_words.add(original)
    return result

given_input = dict(
    string=["dog", "desserts", "god", "stressed"]
)
output = semordnilap(given_input["string"])
outPutPrint(given_input, output)

given_input = dict(
    string=["aaa", "bbbb"]
)
output = semordnilap(given_input["string"])
outPutPrint(given_input, output)
