# Problem Description: https://open.kattis.com/problems/ljutnja

''' General Solution:
    1. Read in a height map where a height -> occurances of that height.
    2. Reduce heights equally by reducing a height as much as we can towards
    either 0 or towards the height less than that height.
    3. Iterate over the map and sum the square and then print it.
'''

if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    heightMap = {}
    for _ in range(N):
        h = int(input())
        if h in heightMap:
            heightMap[h] += 1
        else:
            heightMap[h] = 1

    heightList = sorted(heightMap.keys())
    while len(heightList) > 0 and M > 0:
        current = heightList.pop()

        if len(heightList) > 0:
            distance = current - heightList[-1]
            width = heightMap[current]
            if distance*width <= M:
                M -= distance*width
                heightMap[heightList[-1]] += heightMap[current]
                heightMap[current] = 0
            else:
                div = M // width
                mod = M % width
                M = 0
                newHeight = current - div
                heightMap[newHeight] = heightMap[current]
                if newHeight != current:
                    heightMap[current] = 0

                heightMap[newHeight] -= mod
                if (newHeight-1) in heightMap:
                    heightMap[newHeight-1] += mod
                else:
                    heightMap[newHeight-1] = mod
        else:
            div = M // heightMap[current]
            mod = M % heightMap[current]
            newHeight = current - div
            heightMap[newHeight] = heightMap[current]
            if current != newHeight:
                heightMap[current] = 0

            heightMap[newHeight] -= mod
            if (newHeight - 1) in heightMap:
                heightMap[newHeight - 1] += mod
            else:
                heightMap[newHeight - 1] = mod

    #print(heightMap)
    total = 0
    for key in heightMap.keys():
        total += (key**2)*heightMap[key]

    print(total)
