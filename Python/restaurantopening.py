# Input size is quite low so lets do a brute force solution:
def manhattanDist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1 - y2)

# Input:
n,m = list(map(int, input().split()))
residens = []
for rows in range(n):
    residens.append(list(map(int, input().split())))

# Find distances in O(n^4):
smallestDist = 10001*5100
for x1 in range(m):
    for y1 in range(n):
        dist = 0
        for x2 in range(m):
            for y2 in range(n):
                dist += manhattanDist(x1,y1,x2,y2)*(residens[y2])[x2]

        if dist < smallestDist:
            smallestDist = dist

print(smallestDist)
