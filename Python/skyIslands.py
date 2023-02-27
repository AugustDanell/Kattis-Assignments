def visitAll(start, matrix):
    visited = {start : True}
    toVisit = list(matrix[start].keys())
    visitedNodes = 0

    while(len(toVisit) > 0):
        node = toVisit.pop(0)

        if not visited.__contains__(node):
            visited[node] = True
            visitedNodes += 1
            if visitedNodes == len(matrix) - 1:
                return "YES"

        for nextNode in list(matrix[node].keys()):
            if not visited.__contains__(nextNode):
                toVisit.append(nextNode)

    return "NO"

N,M = list(map(int, input().split()))
adjMatrix = {}
for i in range(N):
    adjMatrix[i+1] = {}


for i in range(M):
    a,b = list(map(int, input().split()))
    adjMatrix[a][b] = True
    adjMatrix[b][a] = True

if N == 1:
    print("YES")
else:
    print(visitAll(1, adjMatrix))
