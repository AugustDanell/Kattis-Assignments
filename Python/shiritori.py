calledOutWords = {}
turns = (int(input()))
turns = turns - 1

start = input()
calledOutWords[start] = start
lastLetter = start[-1]
playerOneTurn = False
brokenGame = False

for i in range(turns):
    word = input()
    if(not word[0] == lastLetter or calledOutWords.__contains__(word)):
        brokenGame = True
        break
    else:
        lastLetter = word[-1]
        calledOutWords[word] = word
        playerOneTurn = not playerOneTurn

if(brokenGame):
    if(playerOneTurn):
        print("Player 1 lost")
    else:
        print("Player 2 lost")
else:
    print("Fair Game")