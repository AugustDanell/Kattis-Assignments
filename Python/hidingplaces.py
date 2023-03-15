# Kattis Assignment: https://open.kattis.com/problems/hidingplaces

# Testfunction to print a chessboard neatly:
def prettyPrint(turn, visited):
    print("Chessboard on turn {0}:".format(turn))
    visitedNodes = 0
    for i in range(1, len(visited)+1):
        row = visited[i]
        visitedNodes += len(row)
        print((i), row, "length:", len(row))
    print("Total Visits:", visitedNodes)

# Two helper functions to convert from Ascii and back again:
def convertFromChrToNum(c):
    return ord(c) -96
def convertFromNumToChr(n):
    return chr(96+n)

# This function takes in a tuple (x,y) and converts it into chess coordinates:
def formatTuple(t):
    x,y = t
    return "{0}{1}".format(convertFromNumToChr(x), y)

# Function to initialize the chessboard (Was never used because nested dictionaries were easier)
def createChessBoard():
    chessBoard = []
    for i in range(8):
        l = []
        for j in range(8):
            l.append(False)
        chessBoard.append(l)
    return chessBoard

# This is a function we pass as a key to the Python sorted function to explain how we want to sort our tuples:
def sortingValue(t):
    x,y = t
    return -x + y*10

# Function to return eligble moves of 8 possible ones:
def getEligbleMoves(x,y, visited):
    l = []
    if x > 2:
        if y < 8:
            l.append((x-2, y+1))
        if y > 1:
            l.append((x-2, y-1))

    if x < 7:
        if y < 8:
            l.append((x+2, y+1))
        if y > 1:
            l.append((x+2, y-1))

    if y > 2:
        if x < 8:
            l.append((x+1, y-2))
        if x > 1:
            l.append((x-1, y-2))

    if y < 7:
        if x < 8:
            l.append((x+1, y+2))
        if x > 1:
            l.append((x-1, y+2))

    # Remove already visited nodes as non-elgible and mark the rest as visited:
    index = 0
    while index < len(l):
        x,y = l[index]
        if visited[x].__contains__(y):
            l.pop(index)
        else:
            visited[x][y] = True
            index += 1
    return l

# The main work horse that performs a BFS and extracts the best hiding places in terms of (x,y).
def itterativeBfsSearch(xStart,yStart):
    turns = 0
    takenSpots = 1
    queue = [[(xStart,yStart)]]
    visited = {1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
    visited[xStart][yStart] = True
    endList = []

    while takenSpots < 64:
        turns +=1
        nextMoves = []
        currentList = queue.pop(0)
        
        # For every element previously visited we append a set of next moves, effectively doing a BFS:
        for element in currentList:
            x,y = element
            eligblesMoves = getEligbleMoves(x,y,visited)
            nextMoves += eligblesMoves
            takenSpots += len(eligblesMoves)
        
        # If all the spots on the board have been marked as visited now we save the next moves as our last moves and exit, otherwise continue on a new set of moves:
        if takenSpots == 64:
            endList = nextMoves
        else:
            queue.append(nextMoves)

    return turns, endList

# 1. Read in the test cases and for each testcase i run the code:
testcases = int(input())
for i in range(testcases):
    # A) Take in input and feed it to the BFS function below:
    x,y = list(input())
    x = convertFromChrToNum(x)
    y = int(y)
    turns, ans = itterativeBfsSearch(x,y)

    # B) The BFS function spits back the hiding places in (x,y). Now we should sort it based on the specification, see sortingValue():
    sortedAns = sorted(ans, key=sortingValue, reverse=True)

    # C) Convert all the hiding places back into the chess form (a-h, 1-8) by passing our function formatTuple on map:
    formatAns = list(map(formatTuple, sortedAns))
    
    # D) Now formatAns should be a list with our answers, sorted and formated. We just apply the join function on that list and pass it into a format string:
    print("{0} {1}".format(turns, " ".join(formatAns)))
