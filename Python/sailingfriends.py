from collections import deque
def BFS(connected, adjlist, start):
    toVisit = deque([start])
    connected[start] = True
    while len(toVisit) > 0:
        node = toVisit.popleft()
        if node in adjlist:
            for nextNode in adjlist[node]:
                if nextNode not in connected:
                    connected[nextNode] = True
                    toVisit.append(nextNode)

if __name__ == "__main__":
    N, B, M = list(map(int, input().split()))
    boatOwners = list(map(int, input().split()))
    connected = {}
    adjList = {}
    for _ in range(M):
        a, b = list(map(int, input().split()))
        if a in adjList:
            adjList[a][b] = True
        else:
            adjList[a] = {b:True}
        if b in adjList:
            adjList[b][a] = True
        else:
            adjList[b] = {a:True}

    for boat in boatOwners:
        if boat not in connected:
            BFS(connected, adjList, boat)

    counter = 0
    for node in range(1, N+1):
        if node not in connected:
            counter += 1
            BFS(connected, adjList, node)

    print(counter)