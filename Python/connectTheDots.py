import sys
def printBoard(s):
    for i in s:
        print("".join(i), end = "")

def giveSubsequent(c):
    if c == "9":
        return "a"
    elif c == "z":
        return "A"
    else:
        # Give the next letter in the alphabet:
        return chr(ord(c)+1)

def connect(coordinates, board):
    if(coordinates.__contains__("0")):
        p = "0"

        while(True):
            n = giveSubsequent(p)
            if(coordinates.__contains__(n)):
                c1 = coordinates[p]
                c2 = coordinates[n]

                if(c1[0] == c2[0]):
                    # Horisontal distance:
                    m1 = min(c1[1], c2[1])
                    m2 = max(c1[1], c2[1])
                    #print(p, n, m1, m2)
                    const =c1[0]

                    for col in range(m1, m2, 1):
                        if(board[const][col] == "."):
                            board[const][col] = "-"
                        elif(board[const][col] == "|"):
                            board[const][col] = "+"

                else:
                    # Vertical distance:
                    m1 = min(c1[0], c2[0])
                    m2 = max(c1[0], c2[0])
                    const = c1[1]

                    for row in range(m1,m2,1):
                        if(board[row][const] == "."):
                            board[row][const] = "|"
                        elif(board[row][const] == "-"):
                            board[row][const] = "+"

                p = n

            else:
                break

    printBoard(board)

#print(giveSubsequent("c"))

coordinates = {}
i = 0
s = []

for line in sys.stdin:
    if(line in ['\n', '\r\n'] ):
        #printBoard(s)
        connect(coordinates, s)
        coordinates = {}
        i = 0
        s = []
        print() # New row for next case
        continue

    #print(line)
    s.append(list(line))

    for j in range(len(line)):
        if(not line[j] == "."):
            coordinates[line[j]] = [i, j]

    i += 1

connect(coordinates, s)
coordinates = {}
i = 0
s = []
print()  # New row for next case

