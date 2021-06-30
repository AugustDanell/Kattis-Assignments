# Problem ID: thisaintyourgrandpaschecker
# Square Matrix Board
dimension = int(input())
board = []
isOk = True

for i in range(dimension):
    board.append([input()])

## INPUT DONE
## 1. Check Rows:

for i in range(dimension):
    W = 0
    B = 0
    prev = ""
    streak = 0

    for j in range(dimension):
        cell = ((((board[i])[0])[j]))
        if(cell == "W"):
            W = W+1
        else:
            B = B+1

        if(prev == cell):
            streak = streak +1
        else:
            streak = 0

        if(streak == 2):
            isOk = False
            break

        prev = cell

    if(not W == B):
        isOk = False
        break

## 2. Check Cols:
for i in range(dimension):
    W = 0
    B = 0
    prev = ""
    streak = 0

    for j in range(dimension):
        cell = ((((board[j])[0])[i]))
        if (cell == "W"):
            W = W + 1
        else:
            B = B + 1

        if (prev == cell):
            streak = streak + 1
        else:
            streak = 0

        if (streak == 2):
            isOk = False
            break

        prev = cell

    if (not W == B):
        isOk = False
        break

## Print:
if(isOk):
    print(1)
else:
    print(0)