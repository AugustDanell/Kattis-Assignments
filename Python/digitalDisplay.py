# Idea:
# We define for every display a function that does just that. What we do then is that for each row we
# join number1, space, number2, space, colon, space, number3, space, number4 into seven strings that are
# outputed in order.

def space():
    l = [["  "], ["  "], ["  "], ["  "], ["  "], ["  "], ["  "]]
    return l

def colon():
    l = [[" "], [" "], ["o"], [" "], ["o"], [" "], [" "]]
    return l

def Zero():
    l = [["+---+"], ["|   |"], ["|   |"], ["+   +"], ["|   |"], ["|   |"], ["+---+"]]
    return l

def One():
    l = [["    +"], ["    |"], ["    |"], ["    +"], ["    |"], ["    |"], ["    +"]]
    return l

def Two():
    l = [["+---+"], ["    |"], ["    |"], ["+---+"], ["|    "], ["|    "], ["+---+"]]
    return l

def Three():
    l = [["+---+"], ["    |"], ["    |"], ["+---+"], ["    |"], ["    |"], ["+---+"]]
    return l

def Four():
    l = [["+   +"], ["|   |"], ["|   |"], ["+---+"], ["    |"], ["    |"], ["    +"]]
    return l

def Five():
    l = [["+---+"], ["|    "], ["|    "], ["+---+"], ["    |"], ["    |"], ["+---+"]]
    return l

def Six():
    l = [["+---+"], ["|    "], ["|    "], ["+---+"], ["|   |"], ["|   |"], ["+---+"]]
    return l

def Seven():
    l = [["+---+"], ["    |"], ["    |"], ["    +"], ["    |"], ["    |"], ["    +"]]
    return l

def Eight():
    l = [["+---+"], ["|   |"], ["|   |"], ["+---+"], ["|   |"], ["|   |"], ["+---+"]]
    return l

def Nine():
    l = [["+---+"], ["|   |"], ["|   |"], ["+---+"], ["    |"], ["    |"], ["+---+"]]
    return l

while(True):
    query = input()
    if(query == "end"):
        print(query)
        break
    else:
        data = list(query)

        #print(data)
        D = []
        for i in range(5):
            c = data[i]
            if(c == "0"):
                D.append(Zero())

            elif (c == "1"):
                D.append(One())

            elif (c == "2"):
                D.append(Two())

            elif (c == "3"):
                D.append(Three())

            elif (c == "4"):
                D.append(Four())

            elif (c == "5"):
                D.append(Five())

            elif (c == "6"):
                D.append(Six())

            elif (c == "7"):
                D.append(Seven())

            elif (c == "8"):
                D.append(Eight())

            elif (c == "9"):
                D.append(Nine())

            if(i == 1):
                D.append(space())
                D.append(colon())


            if(i < 4 and not i == 1):
                D.append(space())

        for i in range(7):
            temp = []
            #print(D)
            for j in range(len(D)):
                temp.append(D[j][i][0])
                #print(temp)

            print("".join(temp))

        print() # Two new rows
        print()