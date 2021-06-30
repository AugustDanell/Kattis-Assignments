import copy

def beatenBy(m):
    if(m == "P"):
        return "S"
    elif(m == "S"):
        return "R"
    elif(m == "R"):
        return "P"

# Idea:
# Iterate through the board and ask yourself, is the piece at
# i,j beaten by an adjacent piece. For each time this is true,
# save that and upon the end of the turn, turn every such case
# into whatever beats that piece:

# E.G: R P S P R
# Iterate through, R is beaten by paper, P is beaten by S, S unbeaten..
# 1,2,4,5 are beaten, so the transform becomes: P S S S P.

cases = int(input())
for i in range(cases):
    data = input().split()
    rows = int(data[0])
    cols = int(data[1])
    loops = int(data[2])

    board = []
    for j in range(rows):
        board.append(list(input()))

    # Iterative transform:
    while(loops > 0):
        noEnemies = True
        newBoard = copy.deepcopy(board)
        for r in range(rows):
            for c in range(cols):
                # 'enemy' should beat m, beatenBy(m):
                # Returns what m is beaten by, stored in 'enemy'

                enemy = beatenBy(board[r][c])
                if(r > 0):
                    if(board[r-1][c] == enemy):
                        newBoard[r][c] = enemy
                        noEnemies = False
                        continue

                if(r < rows-1):
                    if(board[r+1][c] == enemy):
                        newBoard[r][c] = enemy
                        noEnemies = False
                        continue

                if(c > 0):
                    if(board[r][c-1] == enemy):
                        newBoard[r][c] = enemy
                        noEnemies = False
                        continue

                if(c < cols-1):
                    if(board[r][c+1] == enemy):
                        newBoard[r][c] = enemy
                        noEnemies = False
                        continue

                #print(board)

        if(noEnemies):
            break
        board = copy.deepcopy(newBoard)# Transform
        loops -= 1

    for j in range(rows):
        print("".join(board[j]))