if __name__ == "__main__":
    N, H = list(map(int,input().split()))
    upMap = {}
    downMap = {}
    isUp = True

    for _ in range(N):
        if isUp:
            length = int(input())
            if length in upMap:
                upMap[length] += 1
            else:
                upMap[length] = 1
        else:
            length = H - int(input()) +1
            if length in downMap:
                downMap[length] += 1
            else:
                downMap[length] = 1
        isUp = not isUp

    levelMap = {}
    downCounter = 0
    for level in range(H, 0, -1):
        if level in upMap:
            downCounter += upMap[level]
        levelMap[level] = downCounter

    #print(downMap)
    upCounter = 0
    for level in range(1,H+1):
        if level in downMap:
            upCounter += downMap[level]
        levelMap[level] += upCounter

    minVal = float('inf')
    for key in levelMap:
        localVal = levelMap[key]
        minVal = min(minVal, localVal)

    occCounter = 0
    for key in levelMap:
        if levelMap[key] == minVal:
            occCounter += 1

    print(minVal, occCounter)

    #print(levelMap)
