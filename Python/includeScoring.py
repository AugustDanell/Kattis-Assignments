# Problem Description: https://open.kattis.com/problems/includescoring

'''  General Solution:
     1. Read in the data and store an id for each person (in the order they are read in).
     2. Calculate how much points each person has recieved with the individualScoring() function.
     3. Use that as a sorting value to sort a list of people.
     4. Create bundles, i.e, if x people have the same score they are bundled together.
     This bundled list is sorted.
     5. Use the bundled list in ACMscoring() to calculate each persons score within the bundle.
     For example, if one bundle has 2th, 3th and 4th place, each person within the bundle has their
     value set to (2th + 3th + 4th)/3 (rounded up). ACMscoring then returns the hashmap.
     6. Just iterate over 1..n (inclusively) and print the score of corresponding map value.
'''

import math

def individualScore(l):
    problemWeight = 3010*(10**15)
    penaltyWeight = 3010
    return l[0]*problemWeight - l[1]*penaltyWeight - l[2]

def bundle(l):
    bundledList = []
    currentBundle = []
    lastScore = -1
    for i in range(len(l)):
        person = l[i]
        if person[0] == lastScore:
            currentBundle.append(person)
        else:
            bundledList.append(currentBundle)
            currentBundle = [person]
            lastScore = person[0]
    if currentBundle != []:
        bundledList.append(currentBundle)
    return bundledList

def getACMPoints(n):
    switch = {1: 100, 2: 75, 3: 60, 4: 50, 5: 45,
              6: 40, 7: 36, 8:32, 9:29, 10: 26,
              11: 24, 12: 22, 13: 20, 14: 18, 15: 16,
              16: 15, 17: 14, 18: 13, 19: 12, 20: 11,
              21: 10, 22: 9, 23: 8, 24: 7, 25: 6,
              26: 5, 27: 4, 28: 3, 29: 2, 30: 1}
    if n in switch:
        return switch[n]
    else:
        return 0

def ACMscoring(bundledList):
    acmMap = {}
    counter = 0
    for bundle in bundledList:
        score = 0
        for person in bundle:
            counter += 1
            score += getACMPoints(counter)

        for person in bundle:
            acmMap[person[-2]] = math.ceil(score/len(bundle)) + person[-1]
    return acmMap

if __name__ == "__main__":
    extrapoints = {}
    N = int(input())
    people = []
    for id in range(1, N+1):
        solved, timePenalty, lastPenalty, extrapoint = list(map(int,input().split()))
        person = [individualScore([solved, timePenalty, lastPenalty]), id, extrapoint]
        people.append(person)

    sortedPeople = list(sorted(people, key = lambda x: x[0], reverse=True))
    bundledList = bundle(sortedPeople)
    acmMap = ACMscoring(bundledList)

    for i in range(1,N+1):
        print(acmMap[i])
