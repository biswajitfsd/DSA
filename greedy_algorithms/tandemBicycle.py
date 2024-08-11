from lib.outPutPrint import outPutPrint


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    speed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    for r, b in zip(redShirtSpeeds, blueShirtSpeeds):
        speed += max(r, b)
    return speed


data_i, data = (dict(redShirtSpeeds=[5, 5, 3, 9, 2], blueShirtSpeeds=[3, 6, 7, 2, 1], fastest=False),
                dict(redShirtSpeeds=[5, 5, 3, 9, 2], blueShirtSpeeds=[3, 6, 7, 2, 1], fastest=False))
output = tandemBicycle(data_i['redShirtSpeeds'], data_i['blueShirtSpeeds'], data_i['fastest'])
outPutPrint(data, output)
