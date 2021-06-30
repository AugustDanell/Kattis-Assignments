def moveTopToBack(cards, position):
    tempCard = cards[0]
    tempPosition = position[0]
    endIndex = len(cards) -1
    for i in range(endIndex):
        cards[i] = cards[i+1]
        position[i] = position[i+1]

    cards[endIndex] = tempCard
    position[endIndex] = tempPosition

    return cards, position

cases = int(input())
for c in range (cases):
    n = int(input())
    cards = [0 for i in range (n)]
    position = [i for i in range(n)]
    topCards = []

    for i in range (n):
        for j in range(i+1):
            #print("Iteration %d shuffle %d" %(i+1, j+1))
            cards, position = moveTopToBack(cards, position)

        cards[0] = i+1
        topCards.append([cards.pop(0), position.pop(0)])

    orderedCards = []
    for i in range (n):
        for j in range(n):
            pos = (topCards[j])[1]
            card = (topCards[j])[0]
            if(pos == i):
                orderedCards.append(card)

    res = ""
    for i in range(len(orderedCards)):
        res = res + " " + orderedCards[i].__str__()

    print(res[1:])