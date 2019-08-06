"""Convert hex to base 64"""


def hex2bin(number):
    ans = 0
    hexdict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    for x in range(len(number)):
        ans <<= 4
        ans += hexdict.get(number[x])
    return ans


def tobase64(zero264):
    if 25 >= zero264 >= 0:
        return chr(zero264+65)
    if 51 >= zero264 >= 26:
        return chr(zero264 - 26 + 97)
    if 61 >= zero264 >= 52:
        return chr(zero264 - 52 + 48)
    if zero264 == 62:
        return '+'
    if zero264 == 63:
        return '/'



def bin2base64(number):
    ans = ""
    while number != 0:
        zero264 = (number % 64)
        number >>= 6
        ans = str(tobase64(zero264)) + ans
    return ans


def hex2base64(number):
    binnum = hex2bin(number)
    asciinum = bin2base64(binnum)
    return asciinum


print(hex2base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
