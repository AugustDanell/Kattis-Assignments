# A solution to the problem: https://open.kattis.com/problems/moneymatters


def bfs(adj_matrix, visited, node, debt_map):
    """A BFS algorithm that keep tracks of the balance within a connected graph"""
    to_visit = [node]
    balance = 0
    visited[node] = True
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        balance += debt_map[current]

        for v2 in adj_matrix[current].keys():
           if visited.__contains__(v2):
               continue
           else:
               to_visit.append(v2)
               visited[v2] = True

    return balance == 0

# 1. Input, initiate dept for every person: 
V,E = list(map(int,input().split()))
debt_map = {}
for i in range(V):
    debt_map[i] = int(input())

# 2. Read in Adjacency Matrix:
adj_matrix = {}
for _ in range(E):
    v1,v2 = list(map(int,input().split()))

    if adj_matrix.__contains__(v1):
        adj_matrix[v1][v2] = True
    else:
        adj_matrix[v1] = {v2:True}

    if adj_matrix.__contains__(v2):
        adj_matrix[v2][v1] = True
    else:
        adj_matrix[v2] = {v1:True}

# 3. Initiate a hashmap of visited nodes and flag if it is impossible to visit all.
visited = {}
impossible = False
for v in range(V):
    if(visited.__contains__(v)):
        continue
    else:
        # 4. Do a BFS to see if a network of people can be satisfied. If they can we continue with every other networks. Else Break.
        if not bfs(adj_matrix, visited, v, debt_map):
            impossible = True
            break

if(impossible):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
