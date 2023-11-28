# Problem Description: https://open.kattis.com/problems/heroesofvelmar

def calculatePower(cards, isSecond = False):
    power = 0
    powerMap = {
        "Shadow" : 6,
        "Gale" : 5,
        "Ranger" : 4,
        "Anvil" : 7,
        "Vexia" : 3,
        "Guardian" : 8,
        "Thunderheart": 6,
        "Frostwhisper": 2,
        "Voidclaw" : 3,
        "Ironwood" : 3,
        "Zenith" : 4,
        "Seraphina": 1,
    }
    for card in cards:
        if card == "Zenith" and isSecond:
            power += 5
        elif card == "Seraphina":
            power += len(cards)-1
        elif card == "Thunderheart" and len(cards) >= 4:
            power += 6
        power += powerMap[card]
    return power

if __name__ == "__main__":

    rounds = []
    for round in range(1,3+1):
        playerOne = input().split()
        playerTwo = input().split()
        p1 = calculatePower(playerOne[1:], round == 2)
        p2 = calculatePower(playerTwo[1:], round == 2)
        rounds.append([p1, p2])

    #print(rounds)
    # Check rounds:
    w1 = 0
    t1 = 0
    w2 = 0
    t2 = 0
    for round in rounds:
        t1 += round[0]
        t2 += round[1]
        if round[0] > round[1]:
            w1 += 1
        elif round[1] > round[0]:
            w2 += 1

    if (w1 > w2) or (w1 == w2 and t1 > t2):
        print("Player 1")
    elif (w2 > w1) or (w1 == w2 and t2 > t1):
        print("Player 2")
    else:
        print("Tie")
