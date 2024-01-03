# Problem Description: https://open.kattis.com/problems/cyclicalperiods

if __name__ == "__main__":
    N = int(input())
    occMap = {}
    ansMap = {}
    pointToLetters = {}
    for _ in range(N):
        sData, occData = input().split()
        point = int(sData)
        occurances = list(occData)
        pointToLetters[point] = occurances
        for occurance in occurances:
            if occurance in occMap and occurance not in ansMap:
                cycle = point - occMap[occurance]
                ansMap[occurance] = [cycle, point]
            elif occurance not in occMap:
                occMap[occurance] = point

    # Find longest length:
    longestLength = 0
    for key in ansMap.keys():
        length = ansMap[key][0]
        longestLength = max(length, longestLength)

    # Find earliest point
    earliestPoint = float('inf')
    for key in ansMap:
        if ansMap[key][0] != longestLength:
            continue
        point = ansMap[key][1]
        earliestPoint = min(earliestPoint, point)
    #print(ansMap, earliestPoint)

    # Find eligble Letters
    eligbleLetters = {}
    for key in ansMap:
        if ansMap[key][0] == longestLength and ansMap[key][1] == earliestPoint:
            eligbleLetters[key] = True

    # Print first eligble letter:
    for letter in pointToLetters[earliestPoint]:
        if letter in eligbleLetters:
            print(letter)
            break
