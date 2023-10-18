# Problem: https://open.kattis.com/problems/interplanetarytunnels

from collections import deque

def BFS(start, end, adjList):
    toVisit = deque([[start, 0]])
    visited = {}
    while(len(toVisit) > 0):
        currentPackage = toVisit.popleft()
        currentPlanet = currentPackage[0]
        currentDepth = currentPackage[1]

        if(currentPlanet == end):
            return currentDepth
        elif currentPlanet in adjList:
            for nextNode in adjList[currentPlanet]:
                if(nextNode not in visited):
                    visited[nextNode] = True
                    nextPackage = [nextNode, currentDepth+1]
                    toVisit.append(nextPackage)


if __name__ == "__main__":

    # 1. Read in and init quantities:
    N,M = list(map(int,input().split()))
    A,B = list(map(int,input().split()))
    adjList = {}

    # 2. Read in an undirected Graph:
    for _ in range(M):
        x,y = list(map(int,input().split()))
        if x in adjList:
            adjList[x][y] = True
        else:
            adjList[x] = {y:True}
        if y in adjList:
            adjList[y][x] = True
        else:
            adjList[y] = {x:True}

    # 3. Find the distance using BFS between the two planets:
    distance = BFS(A, B, adjList)

    # 4. Now, since they are both "meeting in the middle" we need to calculate the max that anyone takes
    if(distance % 2 == 0):
        print(distance//2)
    else:
        print(distance//2 + 1)
