# Problem Description: https://open.kattis.com/problems/distracted
'''
    General solution:
    The problem "distracted" is a surprisingly difficult problem with people of different marital status
    including the "unknown" status and we are to discern if is decidable that a married person watches an
    unmarried one, and if decidable, is there such a person, or no?
  
    My main function reads in the data and initializes an adjacency list and a reversed adjacency list.
    Also a hashmap for constant look up of status is used.
    These are feeded into the function logicalCheck() that checks for decidability, and if there is such,
    it returns 1 or 0 (1 for true, 0 for false, pertaining to the question of the problem).

    logicalCheck() checks decidability and then proceeds to use DFSUnmarried for every person that is unmarried.
    The DFS traverses down the chain of people looking at them and returns 2-0, where 2 means that a married person 
    has to be gazed by a married person (For example: M -> ? -> U), regardless what status ? is, the result is true.
    The DFS upgrades the status continously to the function outside, which prints the result finally.
'''

# DFSUnmarried: A function that traverses down a chain of people and returns a number 2-0:
def DFSUnmarried(start, adjList, statusMap):

    # 1. Initiate datastructures:
    toVisit = [start]
    ambiguity = 0

    # 2. Iterate over each person on the stack:
    while (len(toVisit) > 0):

        # 3. Check what the marital status of the person is:
        current = toVisit.pop()
        if current in adjList:
            for next in adjList[current]:
                if statusMap[next] == "m":
                    return 2
                elif statusMap[next] == "u":
                    return ambiguity
                else:
                    toVisit.append(next)
                    ambiguity = 1

    return ambiguity

# logicalCheck: Takes in all the data and prints an answer (initially used for testing):
def logicalCheck(adjList, reversedAdjList, statusMap, startingPoints):
    
    # 1. Check if we ought to initiate undetemined as True:
    undetermined = False
    for person in statusMap:
        if statusMap[person] == "?" and person in reversedAdjList:
            for subject in reversedAdjList[person]:
                if statusMap[subject] in ["m", "?"]:
                    undetermined = True
                    break
            if undetermined:
                break

    # 2. Do DFS searches on chains of unmarried people to find chains like (m -> ? -> ? ... -> u) that will be true:
    found = False
    for startingPoint in startingPoints:
        res = DFSUnmarried(startingPoint, reversedAdjList, statusMap)
        if res == 2:
            found = True
            break
        elif res == 1:
            undetermined = True

    # 3. Return the logical conclusion:
    if found:
        return "1"
    elif undetermined:
        return "?"
    else:
        return "0"


# Driver Code:
if __name__ == "__main__":

    # 1. Read in the data:
    N,L = list(map(int,input().split()))
    statusMap = {}
    reversedAdjList = {}
    adjList = {}
    startingPoints = []

    # 2. Read in marital status into the hashmap:
    for _ in range(N):
        name, status = input().split()
        statusMap[name] = status

    # 3. Read in the adjList and the reversed adjList:
    for _ in range(L):
        data = input().split()
        a,b = data[0], data[2]
        adjList[a] = b
        if statusMap[a] == "u":
            startingPoints.append(a)
        if statusMap[b] == "u":
            startingPoints.append(b)
        if b in reversedAdjList:
            reversedAdjList[b][a] = True
        else:
            reversedAdjList[b] = {a:True}

    # 4. Print the result of the logical check:
    print(logicalCheck(adjList, reversedAdjList, statusMap, startingPoints))
