cities = int(input())
adjMatrix = []
removals = 0
totalLength = 0
for i in range(cities):
    l = list(map(int, input().split()))
    adjMatrix.append(l)
    removals += l.count(-1)
    totalLength += len(l)

print(totalLength - removals)
for i in range(cities):
    for j in range(cities):
        row = adjMatrix[i]
        #print(j, row)
        cost = row[j]

        if not cost == -1:
            print(i+1, j+1, cost)
