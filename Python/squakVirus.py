# Problem: https://open.kattis.com/problems/squawk

# spread: A function that spreads every person to every neighbor
def spread(nextTimeMap, currentTimeStep, time, adjList):
    if currentTimeStep in adjList:
        nextNodes = adjList[currentTimeStep]
        for nextNode in nextNodes:
            if nextNode in nextTimeMap:
                nextTimeMap[nextNode] += time
            else:
                nextTimeMap[nextNode] = time

if __name__ == "__main__":
    # 0. Read in data:
    n,m,s,t = list(map(int,input().split()))

    # 1. Read in a directed graph:
    adjList = {}
    for _ in range(m):
        a,b = list(map(int,input().split()))
        if a in adjList:
            adjList[a][b] = True
        else:
            adjList[a] = {b:True}
        if b in adjList:
            adjList[b][a] = True
        else:
            adjList[b] = {a: True}

    # 2. Iterate over every current timestep:
    currentTimeMap = {s:1}
    for _ in range(t):
        
        # 3. Spread to the neighbors of already infected ones:
        nextTimeMap = {}
        for currentTimeStep in currentTimeMap:
            time = currentTimeMap[currentTimeStep]
            spread(nextTimeMap, currentTimeStep, time, adjList)
        
        # 4. Deep-copy over to the current time map (for a new iteration):
        currentTimeMap = {}
        for nextTimeStep in nextTimeMap:
            currentTimeMap[nextTimeStep] = nextTimeMap[nextTimeStep]
    
    # 5. Iterate over every key and accumulate the value:
    total = 0
    for key in currentTimeMap:
        total += currentTimeMap[key]
        
    # 6. Print the total:
    print(total)
