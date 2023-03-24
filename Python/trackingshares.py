# A solution to the problem: https://open.kattis.com/problems/trackingshares

def getClosest(hashMap, day):
    closest = -1
    for key in hashMap.keys():
        if key <= day and key > closest:
            closest = key

    if closest == -1:
        return False
    return hashMap[closest]

day10 = {10:100}
noDay = {}
assert getClosest(day10, 15) == 100
assert getClosest(noDay, 15) == False
assert getClosest(day10, 9) == False

# 1. Take in input:
C = int(input())
companyMap = {}
daySet = {}

# 2. For every company initiate an internal mapping of days to companys and list days as part of a set, for later:
for i in range(C):
    K = int(input())
    internalMap = {}
    for j in range(K):
        n,d = list(map(int,input().split()))
        internalMap[d] = n
        daySet[d] = True
    companyMap[i] = internalMap

# 3. Initiate a value list that takes in the days and uses the function getClosest to get the companys shares on that day:
valueList = []
for day in list(sorted(daySet.keys())):
    value = 0
    for company in companyMap.keys():
        value += getClosest(companyMap[company], day)
    valueList.append(value)

# 4. Print out the formated values of that list:
print(" ".join(list(map(str,valueList))))
