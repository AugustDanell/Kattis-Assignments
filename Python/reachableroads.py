# Solution to the problem: https://open.kattis.com/problems/reachableroads

# A function that takes in a graph G = (V,E) via an adjacency list, a starting node x and returns all nodes connected to the starting node x:
def connectedNodes(startNode, adjList):
   queue = [startNode]
   visited = {}
   while len(queue) > 0:
      currentNode = queue.pop(0)
      if not visited.__contains__(currentNode):
         queue += adjList[currentNode]
         visited[currentNode] = True

   return list(visited.keys())

# A) Input:
testcases = int(input())
for i in range(testcases):
   nodes = int(input())
   edges = int(input())
   adjList = {}
   nodeList = []

   # B) Init adjacency list:
   for j in range(nodes):
      adjList[j] = []
      nodeList.append(j)

   # C) Append bidirectional connections, i.e, create the undirected graph:
   for j in range(edges):
      v1,v2 = list(map(int, input().split()))
      adjList[v1].append(v2)
      adjList[v2].append(v1)
   
   # D) Take in the list of nodes and start with the first one. Remove every node in the same circuit and increment the counter:
   circuits = 0
   while len(nodeList) > 0:
      circuit = connectedNodes(nodeList[0], adjList)
      for node in circuit:
         nodeList.remove(node)

      if len(nodeList) > 0:
         circuits += 1
   
   # E) Print the amount of circuits found:   
   print(circuits)
