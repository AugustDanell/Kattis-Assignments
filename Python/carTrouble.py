# Problem Description: https://open.kattis.com/problems/cartrouble


# DFS: Performs a depth first search to store traversals:
def DFS(visited, adjList, toVisit):
    while len(toVisit) > 0:
        currentStreet = toVisit.pop()
        if currentStreet in adjList:
            for nextStreet in adjList[currentStreet]:
                if nextStreet not in visited:
                    toVisit.append(nextStreet)
                    visited[nextStreet] = True
    return visited

if __name__ == "__main__":
    # 1. Basic input:
    N = int(input())
    adjList = {}
    orderOfAppearance = []

    # 2. Uni-directional adjList:
    for _ in range(N):
        data = list(map(int, input().split()))
        streetId = data[0]
        orderOfAppearance.append(streetId)
        streets = data[1]
        streetList = data[2:]
        for street in streetList:
            if streetId in adjList:
                adjList[streetId][street] = True
            else:
                adjList[streetId] = {street:True}

    # 3. Make a DFS and register visited streets:
    visited = {0:True}
    toVisit = []
    if 0 in adjList:
        toVisit.append(0)
    visited = DFS(visited, adjList, toVisit)

    # 4. Create two lists for trapped streets and unreachable ones:
    TRAPPED = []
    UNREACHABLE = []
    
    # 5. Iterate over order of appearance:
    allGood = True
    for streetId in orderOfAppearance:
        if streetId == 0:
            continue
        
        # 6. If the street is a trapped, append it:
        newVisited = {}
        toVisit = [streetId]
        newVisited = DFS(newVisited, adjList, toVisit)
        if 0 not in newVisited:
            allGood = False
            TRAPPED.append(streetId)
        
        #7. If the street is unreachable, append it:
        if streetId not in visited:
            allGood = False
            UNREACHABLE.append(streetId)

    # 8. If no problem, print, else print trapped and unreachable ones:
    if allGood:
        print("NO PROBLEMS")
    else:
        for id in TRAPPED:
            print("TRAPPED", id)
        for id in UNREACHABLE:
            print("UNREACHABLE", id)
