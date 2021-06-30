def rankUp(currentRank, stars):
    if(currentRank <= 25 and currentRank >= 21):
        if(stars > 2):
            return stars-2, currentRank-1

    if(currentRank <= 20 and currentRank >= 16):
        if(stars>3):
            return stars-3, currentRank-1

    if(currentRank <= 15 and currentRank >= 11):
        if(stars>4):
            return stars-4, currentRank-1

    if(currentRank <= 10 and currentRank >= 1):
        if(stars>5):
            return stars-5, currentRank-1

    return stars, currentRank

def rankDown(currentRank, stars):
    if(stars == -1):
        if(currentRank <= 25 and currentRank >= 21):
            return 0, currentRank
        if(currentRank == 20): ##No effect
            return 0, 20
        if(currentRank <= 19 and currentRank >= 15):
            return 2, currentRank+1
        if(currentRank <= 14 and currentRank >= 10):
            return 3, currentRank+1
        if(currentRank <= 9 and currentRank >= 1):
            return 4, currentRank+1

    return stars, currentRank

matchHistory = input()
currentRank = 25
stars = 0
conWins = 0
legend = False

for i in range(len(matchHistory)):
    if(matchHistory[i] == "L"):

        if(currentRank <= 20):
            stars = stars - 1

        conWins = 0
        stars, currentRank = rankDown(currentRank, stars)
    else:
        conWins = conWins +1
        if(conWins >= 3 and currentRank >= 6):
            stars = stars + 2
        else:
            stars = stars + 1
        stars, currentRank = rankUp(currentRank,stars)

    if(currentRank == 0):
        legend = True

    #print(stars, currentRank)

if(legend):
    print("Legend")
else:
    print(currentRank)