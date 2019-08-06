def hex2bin(number):
    ans = 0
    hexdict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    for x in range(len(number)):
        ans <<= 4
        ans += hexdict.get(number[x])
    return ans


def xor(first, second):
    return first ^ second


def num2hex(number):
    ans = ""
    hexdict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    unhexdict = dict([(value, key) for key, value in hexdict.items()])

    while number != 0:
        hextemp = number % 16
        number >>= 4
        ans = unhexdict.get(hextemp) + ans
    return ans


unhex = hex2bin("1c0111001f010100061a024b53535009181c")
unhex2 = hex2bin("686974207468652062756c6c277320657965")

xored = xor(unhex, unhex2)

final = num2hex(xored)
#print(final)
