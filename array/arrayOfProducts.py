# def arrayOfProducts(array):
#     # Write your code here.
#     result = []
#     for i in range(0, len(array)):
#         mul = 1
#         j = 0
#         while j < len(array):
#             if i != j:
#                 mul *= array[j]
#             j += 1
#         result.append(mul)
#
#     return result
#     pass
#
#
# print(arrayOfProducts([5, 1, 4, 2]))


def arrayOfProducts(array):
    # Write your code here.
    product = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        product[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        product[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return product


print(arrayOfProducts([5, 1, 4, 2]))
