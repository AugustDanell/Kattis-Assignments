# Problem Description: https://open.kattis.com/problems/dominoes2

from collections import deque

# A BFS that creates the domino effect, returns how many dominos were visited (turned over):
def BFS(adjList, toVisit):
    visited = {}
    while(len(toVisit) > 0):
        current = toVisit.popleft()
        if current not in visited:
            visited[current] = True
            if current in adjList:
                for nextNode in adjList[current]:
                    toVisit.append(nextNode)

    return len(visited)

if __name__ == "__main__":
    # 1. Read in data:
    N = int(input())
    for _ in range(N):
        n,m,l = list(map(int,input().split()))
        adjList = {}

        # 2. Insert it into a directed graph:
        for _ in range(m):
            a,b = list(map(int,input().split()))
            if a not in adjList:
                adjList[a] = {b:True}
            else:
                adjList[a][b] = True

        # 3. Initiate data for a BFS:
        fallenDominoMap = {}
        bfsStart = deque([])
        for _ in range(l):
            domino = int(input())
            bfsStart.append(domino)
            fallenDominoMap[domino] = True

        # 4. Print the result of the BFS:
        print(BFS(adjList, bfsStart))
