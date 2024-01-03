def cuts(c, text, cutSize):
    pointer = 0
    cutCounter = 0
    while pointer < len(text):
        if text[pointer] == c:
            pointer += 1
        else:
            pointer += cutSize
            cutCounter += 1
    return cutCounter

if __name__ == "__main__":
    text = input()
    cutSize = int(input())
    bestCuts = -1
    for i in range(97, 122+1):
        c = chr(i)
        localCuts = cuts(c, text, cutSize)
        if bestCuts == -1 or localCuts < bestCuts:
            bestCuts = localCuts

    print(bestCuts)