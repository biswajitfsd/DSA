from lib.outPutPrint import outPutPrint


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    i = 0
    if redShirtHeights[i] < blueShirtHeights[i]:
        while i < len(redShirtHeights):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
            i += 1
    else:
        while i < len(redShirtHeights):
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
            i += 1
    return True


data = dict(
    redShirtHeights=[5, 8, 1, 3, 4],
    blueShirtHeights=[6, 9, 2, 4, 5]
)
output = classPhotos(data["redShirtHeights"], data["blueShirtHeights"])
outPutPrint(data, output)
