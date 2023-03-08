# Kattis Assignment: https://open.kattis.com/problems/empleh

# Map (x,y) coordinates to the chess boards coordinate system:
def mapCoordinates(x,y):
    return (x*4)+2, (y*2)+1

# Helper functions to construct a chess board:
def drawDelimiterRow():
    return list("+---+---+---+---+---+---+---+---+")

def drawStartBlack():
    return list("|:::|...|:::|...|:::|...|:::|...|")

def drawStartWhite():
    return list("|...|:::|...|:::|...|:::|...|:::|")

# Constructs an empty board using the helper functions above:
def constructBoard():
    b = []
    white = True
    for i in range(8):
        if i == 0:
            b.append(drawDelimiterRow())

        if white:
            b.append(drawStartWhite())
        else:
            b.append(drawStartBlack())

        b.append(drawDelimiterRow())

        white = not white

    return b

def printBoard(board):
    for row in board:
        print("".join(row))

def insertPiece(board, dataString, isWhite):
    data = list(dataString)
    piece, hex, num = 0,0,0 # Bad naming calling it hex since it is a keyword.
  
    # Handle special case for peasants:
    if(len(data) == 3):
        piece = data[0]
        hex = data[1]
        num = data[2]
    else:
        hex = data[0]
        num = data[1]
        piece = "p"
        if isWhite:
            piece = "P"

    # Convert coordinates:
    x = ord(hex) - 97
    y = 8 - int(num)
    X,Y = mapCoordinates(x,y)

    # Insert piece:
    board[Y][X] = piece

# Handle Input:
board = constructBoard()
whiteInput = (input())[7:]
blackInput = (input().lower())[7:]

# Check for no white pieces:
if whiteInput.__contains__(","):
    whiteInsertions = whiteInput.split(",")
else:
    whiteInsertions = []
    
# Insert white pieces onto the board:
for whiteInsertion in whiteInsertions:
    insertPiece(board, whiteInsertion, True)

# Check for no black pieces:
if blackInput.__contains__(","):
    blackInsertions = blackInput.split(",")
else:
    blackInsertions = []

# Insert black pieces onto the board:
for blackInsertion in blackInsertions:
    insertPiece(board, blackInsertion, False)

printBoard(board)
