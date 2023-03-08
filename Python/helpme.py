# Kattis Assignment: https://open.kattis.com/submissions/10666864

# Pops the least piece according to what is the flag, white or black (they have different ordering criteria):
def popLeast(l, white = True):
    popIndex = 0
    value = 0

    if white:
        for index in range(len(l)):
            val = (80-l[index][0]) + (800-10*l[index][1])
            if val > value:
                popIndex = index
                value = val
    else:
        for index in range(len(l)):
            val = (80-l[index][0]) + (10*l[index][1])
            if val > value:
                popIndex = index
                value = val


    return l.pop(popIndex)

# Take in a x coordinate and map it to the hex coordinates in chess:
def mapToHex(x):
    return chr(x+97)

# Take care of outputting white pieces:
def printWhitePieces(d):
    outputMapping = {"K":[], "Q":[], "R":[], "B":[], "N":[], "P":[]}
    for piece in d.keys():
        l = d[piece]
        while len(l) > 0:
            appendPiece = piece
            if piece == "P":
                appendPiece = ""

            leastElement = popLeast(l)
            leastElement[0] = mapToHex(leastElement[0])
            outputMapping[piece].append("{2}{0}{1}".format(leastElement[0], leastElement[1], appendPiece))

    outString = outputMapping["K"] + outputMapping["Q"] + outputMapping["R"] + outputMapping["B"] + outputMapping["N"] + outputMapping["P"]
    print("White:", ",".join(outString))

# Take care of outputting black pieces:
def printBlackPieces(d):
    outputMapping = {"k": [], "q": [], "r": [], "b": [], "n": [], "p": []}
    for piece in d.keys():
        l = d[piece]
        while len(l) > 0:
            appendPiece = piece.upper()
            if appendPiece == "P":
                appendPiece = ""

            leastElement = popLeast(l, False)
            leastElement[0] = mapToHex(leastElement[0])
            outputMapping[piece].append("{2}{0}{1}".format(leastElement[0], leastElement[1], appendPiece))


    outString = outputMapping["k"] + outputMapping["q"] + outputMapping["r"] + outputMapping["b"] + outputMapping["n"] + outputMapping["p"]

    print("Black:", ",".join(outString))

# Maps x,y coordinates from taking all characters into consideration into 8x8 chess board:
def mapCoordinates(x,y):
    return [(x-2)//4, 8 - (y-1)//2]

board = []
for i in range(17):
    board.append(input())

whitePieces = {"K":[], "Q":[], "R":[], "B":[], "N":[], "P":[]}
blackPieces = {"k":[], "q":[], "r":[], "b":[], "n":[], "p":[]}

# Scan through the chess board:
x = 2
y = 1
while y < 17:
    # Read in a piece if eligble:
    piece = board[y][x]

    if piece in blackPieces.keys():
        blackPieces[piece].append(mapCoordinates(x,y))
    elif piece in whitePieces.keys():
        whitePieces[piece].append(mapCoordinates(x,y))

    # Incrementation of coordinates:
    x += 4
    if x > 33:
        y += 2
        x = 2

# Output the answers:
printWhitePieces(whitePieces)
printBlackPieces(blackPieces)
