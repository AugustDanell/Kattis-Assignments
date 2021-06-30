def getCoordinates(c):
    if(c == "A"):
        return  0,0
    if (c == "B"):
        return 1, 0
    if (c == "C"):
        return 2, 0
    if (c == "D"):
        return 3, 0

    if (c == "E"):
        return 0, 1
    if (c == "F"):
        return 1, 1
    if (c == "G"):
        return 2, 1
    if (c == "H"):
        return 3, 1

    if (c == "I"):
        return 0, 2
    if (c == "J"):
        return 1, 2
    if (c == "K"):
        return 2, 2
    if (c == "L"):
        return 3, 2

    if (c == "M"):
        return 0, 3
    if (c == "N"):
        return 1, 3
    if (c == "O"):
        return 2, 3

def manhattanDistance(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

game = []
for i in range(4):
    game.append(input())

sum = 0
for i in range(4):
    for j in range(4):
        letter = game[i][j]

        if(not letter == "."):
            x1,y1 = getCoordinates(letter)

            letter2 = chr(65 + i*4 + j)
            x2 = j
            y2 = i
            #print(letter)
            #print(letter2)
            sum = sum + manhattanDistance(x1,x2,y1,y2)

print(sum)