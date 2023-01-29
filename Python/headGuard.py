import sys

def countString(str):
    prevChar = ""
    outStr = ""
    countedItems = 0
    for char in str:
        if(countedItems == 0):
            countedItems = 1
            prevChar = char
            continue

        if prevChar == char:
            countedItems += 1
        else:
            outStr += "{0}{1}".format(countedItems, prevChar)
            countedItems = 1
        prevChar = char

    if countedItems > 1:
        outStr += "{0}{1}".format(countedItems, prevChar)

    return outStr

for line in sys.stdin:
    print(countString(line))
