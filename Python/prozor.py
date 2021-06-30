for i in range(1, 1):
    print("Yes")

data = input()
split = data.split()

rows = int(split[0])
cols = int(split[1])
rack = int(split[2]) # Racket is a square matrix

board = []
for i in range(rows):
    board.append(input())

killRow = (rack-2)
killCol = (rack-2)
killMax = 0
indMax = []
for i in range(1, rows-rack+2):
    for j in range(1, cols-rack+2):
        killCount = 0
        for k in range(killRow):
            for l in range(killCol):
               if((board[i+k])[j+l] == "*"):
                   killCount = killCount + 1
        if(killCount > killMax):
            killMax = killCount
            indMax = [i,j]  #Top-left corner coordinate

#print(killMax, indMax)

print(killMax)
# Print racket
for i in range(rows):
    s = ""
    x = indMax[0]
    y = indMax[1]
    for j in range(cols):
        if(i+1 == x and j+1 == y):
            s = s + "+"
        elif(i+1 == x and j+1 == y+rack-1):
            s = s + "+"
        elif(i+1 == x and j+1 > y and j+1 < y + rack -1):
            s = s + "-"
        elif(i+1 == x+rack-1 and j+1 > y and j+1 < y + rack -1):
            s = s + "-"
        elif(j+1 == y and i+1 == x + (rack-1)):
            s = s+ "+"
        elif (j + 1 == y+rack-1 and i + 1 == x + (rack - 1)):
            s = s + "+"
        elif(j+1 == y and i+1 > x and i+1 < x + rack-1):
            s = s + "|"
        elif (j + 1 == y+rack-1 and i + 1 > x and i + 1 < x + rack - 1):
            s = s + "|"
        else:
            s = s + board[i][j]

    print(s)