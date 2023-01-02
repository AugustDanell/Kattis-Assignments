# Slow & Lazy solution
import sys

def convert(s):
    return int(s, 16)

def handleInput(s):
    flag = False
    out = ""
    l = []

    for i in range(len(s) - 1):
        if(s[i] == "0" and (s[i+1] == "X" or s[i+1] == "x")):
            if(flag):
                l.append(out)
            flag = True
            out = ""

        if(flag):
            out += s[i]

    out += s[len(s)-1]
    l.append(out)
    return l

hex = ["0", "1", "2", "3", "4", "5", "6","7","8","9","a","b","c","d","e","f"]
hexStrings = []
currentStr = ""
triggered = False

for inLine in sys.stdin:
    inStrings = handleInput(inLine)
    for line in inStrings:
        hexString = line[0:2]
        line = line [2:]

        for char in line:
            if(not hex.__contains__(char.lower())):
                break
            else:
                hexString += char
        hexStrings.append(hexString)

for hexString in hexStrings:
    print(hexString, convert(hexString))
