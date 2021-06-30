import sys

def getSum(d,l):
    sum = 0
    for i in range(1,len(l)):
        sum += d[l[i]]

    return sum

categories = int(input())

wordDict = {}
categoryList = []

for i in range(categories):
    category = input().split()
    row = [category[0]]
    for j in range(2,len(category)):
        row.append(category[j])
        wordDict[category[j]] = 0
    categoryList.append(row)

# ok
for line in sys.stdin:
    data = line.split()
    for i in range(len(data)):
        if(data[i] in wordDict):
            wordDict[data[i]] += 1
# ok

finalList = []
max = 0
for i in range(categories):
    s = getSum(wordDict, categoryList[i])
    #print(categoryList[i][0], s)
    if(s == max):
        finalList.append(categoryList[i][0])
    elif(s > max):
        max = s
        finalList = [categoryList[i][0]]

finalList.sort()
for i in range(len(finalList)):
    print(finalList[i])