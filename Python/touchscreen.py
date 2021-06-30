# Problem ID: touchscreenkeyboard
def manhattanDistance(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)

def assignCoordinates(c):
    if(c == "q"):
        return 0,0
    if(c == "w"):
        return 1,0
    if(c == "e"):
        return 2,0
    if(c == "r"):
        return 3,0
    if(c == "t"):
        return 4,0
    if(c == "y"):
        return 5,0
    if(c == "u"):
        return 6,0
    if(c == "i"):
        return 7,0
    if(c == "o"):
        return 8,0
    if(c == "p"):
        return 9,0

    if(c == "a"):
        return 0,1
    if(c == "s"):
        return 1,1
    if(c == "d"):
        return 2,1
    if(c == "f"):
        return 3,1
    if(c == "g"):
        return 4,1
    if(c == "h"):
        return 5,1
    if(c == "j"):
        return 6,1
    if(c == "k"):
        return 7,1
    if(c == "l"):
        return 8,1

    if(c == "z"):
        return 0,2
    if(c == "x"):
        return 1,2
    if(c == "c"):
        return 2,2
    if(c == "v"):
        return 3,2
    if(c == "b"):
        return 4,2
    if(c == "n"):
        return 5,2
    if(c == "m"):
        return 6,2

def selectionSort(wordList):
    length = len(wordList)
    for i in range(length):
        min = wordList[i]
        for j in range(i, length):
            current = wordList[j]
            if(current[1] < min[1]):
                wordList[j] = wordList[i]
                wordList[i] = current
                min = current

            if(current[1] == min[1] and min[0] > current[0]):
                wordList[j] = wordList[i]
                wordList[i] = current
                min = current
        print(min[0],min[1])

    return wordList

def quicksort(l,lower,upper):
    if(lower < upper):
        index = firstElementPartition(l, lower, upper)
        quicksort(l, lower, index-1)
        quicksort(l, index + 1, upper)

def firstElementPartition(l,lower,upper):
    i = lower-1
    pivot = l[lower]
    for j in range(lower, upper):
        if (l[j] <= pivot):
            i = i+1
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
    temp = l[i+1]
    l[i+1] = l[upper]
    l[upper] = temp

    return (i+1)

def mainSelectionSort():
    cases = int(input())
    globalList = []
    for i in range(cases):
        wordList = []
        data = input().split()
        word = data[0]
        words = int(data[1])

        for j in range(words):
            distance = 0
            word2 = input()
            for k in range (len(word)):
                x1, y1 = assignCoordinates(word[k])
                x2, y2 = assignCoordinates(word2[k])
                distance = distance + manhattanDistance(x1, x2, y1, y2)

            wordList.append([word2,distance])

        wordList = selectionSort(wordList)

mainSelectionSort()


