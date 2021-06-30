guess = 1
guessList = []
directionList = []

while(not guess == 0):
    guess = int(input())
    if(guess == 0):
        break

    direction = input()

    if(direction == "too high" or direction == "too low"):
        guessList.append(guess)
        directionList.append(direction)

    elif(direction == "right on"):
        ans = guess
        honestGame = True
        #print(guessList)
        for i in range(len(guessList)):
            g = guessList[i]
            d = directionList[i]

            if(g >= ans and d == "too low"):
                honestGame = False
                break
            elif(g <= ans and d == "too high"):
                honestGame = False
                break


        if(honestGame):
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        guessList = []
        directionList = []
