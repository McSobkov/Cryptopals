"""Convert hex to base 64"""
def hex2bin(number):
    ans = 0
    hexdict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
               "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    for x in range(len(number)):
        ans << 8
        ans += hexdict.get(number[x])
    return ans



def hex2base64(number):
    binnum = hex2bin(number)
    ans = ""
    return binnum


print(hex2base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
