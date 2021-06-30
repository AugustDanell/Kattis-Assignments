# Two schemes, merging and moving
# always begining at i = 1:
def leftShift(R):
    canShift = True
    i = 1
    bools = [False, False, False,False]
    while(canShift):
         if(not(R[i-1] == 0) and (R[i-1] == R[i]) and not(bools[i-1])):
             R[i-1] = 2*R[i-1]
             R[i] = 0
             bools[i-1] = True
             if(i >= 2):
                 bools[i-2] = True
             i = 1
             continue

         if(R[i-1] == 0 and not(R[i] == 0)):
             R[i-1] = R[i]
             R[i] = 0
             i = 1
             continue

         i = i+1
         if(i == 4):
             canShift = False

    return R

def rightShift(R):
    canShift = True
    i = -2
    bools = [False, False, False, False]
    while (canShift):
        if (not (R[i + 1] == 0) and (R[i + 1] == R[i]) and not (bools[i+1])):
            R[i + 1] = 2 * R[i + 1]
            R[i] = 0
            bools[i+1] = True
            if(i<=-3):
                bools[i+2] = True
            i = -2
            continue

        if (R[i + 1] == 0 and not (R[i] == 0)):
            R[i + 1] = R[i]
            R[i] = 0
            i = -2
            continue

        i = i - 1
        if (i == -5):
            canShift = False

    return R

def transponante(m):
    matrix = [[],[],[],[]]
    for i in range (4):
        for j in range(4):
            matrix[j].append((m[i])[j])
    return  matrix

board = []
for i in range (4):
    inp = input()
    split = inp.split()
    board.append([int(split[0]), int(split[1]), int(split[2]), int(split[3])])

up = False
down = False
left = False
right = False


inp = input()

if(inp == "0"):
    left = True
elif(inp == "1"):
    up = True
elif(inp == "2"):
    right = True
else:
    down = True

if(left):
    for i in range(4):
        board[i] = leftShift(board[i])

if(up):
    board = transponante(board)
    for i in range(4):
        board[i] = leftShift(board[i])
    board = transponante(board)

if(down):
    board = transponante(board)
    for i in range(4):
        board[i] = rightShift(board[i])
    board = transponante(board)

if(right):
    for i in range(4):
        board[i] = rightShift(board[i])


for i in range(4):
    print("%d %d %d %d" % ((board[i])[0], (board[i])[1], (board[i])[2], (board[i])[3]))

