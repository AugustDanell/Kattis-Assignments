# A solution to the problem: https://open.kattis.com/problems/soundex
import sys

# 1. Initiate a mapping from the letters to their value according to the problem:
letterMap = {
    "B" : 1, "F":1, "P":1, "V":1,
    "C": 2, "G":2, "J":2, "K":2, "Q":2, "S":2, "X":2, "Z":2,
    "D":3, "T":3,
    "L":4,
    "M":5, "N":5,
    "R":6}

# 2. Read in line by line, have a flag for previous character and a list for values:
for line in sys.stdin:
    prev = ""
    l = []

    # 3. For every character, if it has the same sound as the previous one or if it does not exist, skip. Else append:
    for c in line:
        if (letterMap.__contains__(c) and letterMap.__contains__(prev) and letterMap[c] == letterMap[prev]):
            prev = c
            continue
        elif not letterMap.__contains__(c):
            prev = c
            continue
        else:
            l.append(str(letterMap[c]))
        prev = c
    
    # 4. Print the answer:
    print("".join(l))
