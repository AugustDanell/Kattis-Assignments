# Identify the pattern and create a binary string, then parse it to an int at the end.

quadkey = input()
binX = ""
binY = ""

for x in quadkey:
    if(x == "1"):
        binX += "1"
        binY += "0"
    elif(x == "2"):
        binX += "0"
        binY += "1"
    elif(x == "3"):
        binX += "1"
        binY += "1"
    else:
        binX += "0"
        binY += "0"

print(len(quadkey), int(binX, 2), int(binY, 2))
