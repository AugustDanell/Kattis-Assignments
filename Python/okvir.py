def printFrame(w):
    for i in range(len(w)):
        print(w[i])

def frame(words,n,m,u,l,r,d):
    # m = antal ord
    # n = längd

    returnFrame = []
    frame = []
    dot = False
    rowLength = l+r+m
    rows = u + d + n

    startDot = False

    for i in range(rows):
        appendex = ""
        for j in range(rowLength):
            if(j == 0 and startDot):
                appendex = appendex + "."
                dot = False
                startDot = False
            elif(j==0):
                appendex = appendex + "#"
                startDot = True
                dot = True
            else:
                #General non-start case:
                if(dot):
                    appendex = appendex + "."
                    dot = False
                else:
                    appendex = appendex + "#"
                    dot = True

        frame.append(list(appendex))
        #print(frame)

    #Ok, now we insert a word:
    for i in range(len(words)):
        for j in range(len(words[0])):
            letter = (words[i])[j]
            (frame[U+i])[j+L] = letter

    for i in range(len(frame)):
        string = ""
        returnFrame.append(string.join(frame[i]))

    return returnFrame

inp = input()
split = inp.split()
M = int(split[0])
N = int(split[1])

inp = input()
split = inp.split()
U = int(split[0])
L = int(split[1])
R = int(split[2])
D = int(split[3])

words = []
for i in range(M):
    words.append(input())

printFrame(frame(words, M,N, U, L, R, D))