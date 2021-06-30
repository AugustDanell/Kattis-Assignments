import sys
board = []

# Problem: Maybe the recursive removal scheme reaches stack overflow?
# We can make a remedy by rewriting it itteratively.

def ittRemoval(i,j,rows,cols):
    None

sys.setrecursionlimit(10000)
def recursiveRemoval(i, j,rows,cols):
    board[i][j] = "#"
    if(i > 0):
        if(board[i-1][j] == "-"):
            recursiveRemoval(i-1, j, rows, cols)

    if(j > 0):
        if(board[i][j-1] == "-"):
            recursiveRemoval(i, j-1, rows, cols)

    if(i < rows-1):
        if(board[i+1][j] == "-"):
            recursiveRemoval(i+1, j, rows, cols)

    if(j < cols-1):
        if(board[i][j+1] == "-"):
            recursiveRemoval(i, j+1, rows, cols)

    return board


case = 1
for line in sys.stdin:
    data = line.split()

    rows = int(data[0])
    cols = int(data[1])
    board = []

    for i in range(rows):
        board.append(list (input()))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if(board[i][j] == "-"):
                count += 1
                board = recursiveRemoval(i,j, rows, cols)
                #print(board)
    print("Case %d: %d" %(case, count))
    #print("Case %d: %d" %(case, 4**(2-case))) For testing error
    case += 1