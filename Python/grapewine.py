# Problem Description: https://open.kattis.com/problems/grapevine

if __name__ == "__main__":
    # 1. Input data:
    n,m,d = list(map(int,input().split()))
    peopleMap = {}
    for _ in range(n):
        person, t = input().split()
        t = int(t)
        peopleMap[person] = t

    # 2. Create a bidirectional adj list:
    adjList = {}
    for _ in range(m):
        a,b = input().split()
        if a in adjList:
            adjList[a][b] = True
        else:
            adjList[a] = {b:True}
        if b in adjList:
            adjList[b][a] = True
        else:
            adjList[b] = {a:True}
    
    # 3. Initiate data, a start person, a day counter and a map of who has heard the rumor:
    start = input()
    toVisit = [start]
    currentDay = 0
    heardRumor = {start:True}
    
    # 4. Iterate for as long as we can / need to:
    while(currentDay < d and len(toVisit) > 0):
        currentDay += 1
        nextToVisit = []
        
        # 5. Iterate over every rumor spreader:
        while len(toVisit) > 0:
            p1 = toVisit.pop()
            if p1 in adjList:
                
                # 6. For each neighbor, decrement their counter:
                for p2 in adjList[p1]:
                    peopleMap[p2] -= 1
                    
                    # 7. If p2 counter is 0, convert them to a rumor spreader:
                    if peopleMap[p2] == 0:
                        nextToVisit.append(p2)
                        
                    # 8. If p2 has not been included yet, include them as heard rumor:
                    if p2 not in heardRumor:
                        heardRumor[p2] = True
        
        # 9. Deep copy (By Value) the new rumor spreaders:
        for p in nextToVisit:
            toVisit.append(p)

    # 10. Print how many have heard the rumor (-1 for the starting person):
    print(len(heardRumor) -1)


