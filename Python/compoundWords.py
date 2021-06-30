import sys
wordList = []
compoundList = []

for line in sys.stdin:
    data = line.split()
    for i in range(len(data)):
        wordList.append(data[i])

for i in range(len(wordList)):
    for j in range(i+1, len(wordList)):
        compoundWord1 = wordList[i] + wordList[j]
        compoundWord2 = wordList[j] + wordList[i]

        if(not compoundList.__contains__(compoundWord1)):
            compoundList.append(compoundWord1)
        if(not compoundList.__contains__(compoundWord2)):
            compoundList.append(compoundWord2)

compoundList.sort()
for i in range(len(compoundList)):
    print(compoundList[i])
