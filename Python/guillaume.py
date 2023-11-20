if __name__ == "__main__":
    N = int(input())
    letters = list(input())
    while(len(letters) > 0 and letters[-1] == "D"):
        letters.pop()


    A = 0
    G = 0
    D = 0

    bestCount = 0
    bestVal = [0, 0]
    for i in range(len(letters)-1, -1, -1):
        if letters[i] == "A":
            A += 1
        elif letters[i] == "G":
            G += 1

        total = G + A
        if G/(total) > bestCount:
            bestCount = G/total
            bestVal = [G, A]

    if not letters.__contains__("G") and letters.__contains__("A"):
        print("0-1")
    else:
        print("{0}-{1}".format(bestVal[0], bestVal[1]))