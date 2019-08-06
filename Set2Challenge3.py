from Set1Challenge2 import hex2bin

def xorall(number):
    count = 0
    for x in range(255):
        printbool = True
        numclone = number
        ans = ""
        while numclone != 0:
            chrtemp = numclone % 256
            numclone >>= 8
            chrtemp ^= x
            if chrtemp >= 123 or chrtemp <= 31 or 94 >= chrtemp >= 91:
                printbool = False
                break
            ans = chr(chrtemp) + ans
        if printbool:
            count += 1
            print(str(count) + ": " + ans)






binnum = hex2bin("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
xorall(binnum)
