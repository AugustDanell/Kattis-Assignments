# Problem Description: https://open.kattis.com/problems/cantinaofbabel

'''  General Solution:
     a) Create a map of languages -> {<people who can speak it>}
     b) Use this map to create an adjacencyList and a reversedAdjacencyList.
     c) Iterate over each person:
     d) For each person, find the graph using a BFS in normal order and in reversed order.
     e) For both of these graphs, extract the union of elements.
     f) Have a counter, and print the union that is of the highest degree.
'''

from collections import deque

# BFS: Normal Breath First Search:
def BFS(toVisit, adjList):
    visited = {toVisit[0]: True}
    while len(toVisit) > 0:
        currentNode = toVisit.popleft()
        if currentNode in adjList:
            for nextNode in adjList[currentNode]:
                if nextNode not in visited:
                    toVisit.append(nextNode)
                    visited[nextNode] = True
    return visited


if __name__ == "__main__":
    # 1. Do some standard input:
    N = int(input())
    languageToPpl = {}
    people = []

    # 2. Create a map where language -> [<All speakers>]
    for _ in range(N):
        data = input().split()
        person = data[0]
        spoken = data[1]
        understood = data[1:]
        for language in understood:
            if language in languageToPpl:
                languageToPpl[language][person] = True
            else:
                languageToPpl[language] = {person: True}
        people.append([person, spoken])

    # 3. Use the map to reate an adjacency list and a reversed adjacencyList:
    adjList = {}
    revAdjList = {}
    for personData in people:
        a = personData[0]
        spoken = personData[1]
        if spoken in languageToPpl:
            for b in languageToPpl[spoken]:
                if a in adjList:
                    adjList[a][b] = True
                else:
                    adjList[a] = {b: True}

                if b in revAdjList:
                    revAdjList[b][a] = True
                else:
                    revAdjList[b] = {a: True}

    # 4. Iterate over every starting person and find a best list:
    bestUnion = []
    for personData in people:

        # 5. Find every person reachable directly and in reverse:
        person = personData[0]
        start = deque([person])
        path = BFS(start, adjList)
        start = deque([person])
        revPath = BFS(start, revAdjList)

        # 6. Find the union of going both directions in BFS:
        union = []
        for element in path.keys():
            if element in revPath:
                union.append(element)

        # 7. If the local union is the best, then update the best:
        if len(union) > len(bestUnion):
            bestUnion = union

    # 8. Print the answer as N - |bestUnion|
    print(N - len(bestUnion))
