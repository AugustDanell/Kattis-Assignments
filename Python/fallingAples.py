# for i in range(r-1, 0, -1):
#    for j in range(c-1, -1, -1):
#        #print(i, j)
#        if(board[i][j] == "." and board[i-1][j] == "a"):
# print("YOYOYO")
#            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
#            fallen = True


data = input().split()
r = int(data[0])
c = int(data[1])

board = []
for i in range (r):
    board.append(list(input()))

while(True):
    #fallen = False
    # CODE: Look on row above and "pick" down apples.
    for j in range(c):
        fallingPoint = r-1
        i = fallingPoint-1

        if(board[i+1][j] == "#" or board[i+1][j] == "a"):
            fallingPoint -= 1

        while(i >= 0):
            #print("i:", i, "j:", j, "fp:", fallingPoint)

            if(board[i][j] == "#"):
                fallingPoint = i-1
            elif(board[i][j] == "a"):
                board[fallingPoint][j], board[i][j] = board[i][j], board[fallingPoint][j]
                fallingPoint -= 1

            i-= 1

    break

for i in range(r):
    print("".join(board[i]))
