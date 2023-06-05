# 706th Kattis, A Solution To The Problem: https://open.kattis.com/problems/horror

''' General Solution: BFS with multiple starting points.
    1. We declare a to_visit deque with horror movies of HDI = 0.
    2. We declare an adjacency list of movies that are similar.
    3. We feed these values into a BFS.
    4. The BFS will return:
       
       A) if every node is visited: 
          The smallest index in the list of movies with the highest depth.
       
       B) else:
          The smallest index of a non-visited node.
'''

from collections import deque
def BFS(V, to_visit, adj_list, visited):
    max_depth = 0
    max_depth_list = []
    for l in to_visit:
        max_depth_list.append(l[0])
        visited[l[0]] = True
        
    while len(to_visit) > 0:
        current_package = to_visit.popleft()
        current_node = current_package[0]
        visited[current_node] = True
        current_depth = current_package[1]
        if current_node not in adj_list:
            continue

        for next_node in adj_list[current_node].keys():
            if next_node in visited:
                continue
            else:
                new_depth = current_depth + 1
                if new_depth > max_depth:
                    max_depth = new_depth
                    max_depth_list = [next_node]
                elif new_depth == max_depth:
                    max_depth_list.append(next_node)
                to_visit.append([next_node, new_depth])


    if(len(visited) == V):
        return min(max_depth_list)
    else:
        for v in range(V):
            if v not in visited:
                return v

N, H, L = list(map(int,input().split()))
to_visit = deque([])
for node in list(map(int,input().split())):
    to_visit.append([node, 0])

adj_list = {}
for _ in range(L):
    a,b = list(map(int,input().split()))
    if a in adj_list:
        adj_list[a][b] = True
    else:
        adj_list[a] = {b:True}
    if b in adj_list:
        adj_list[b][a] = True
    else:
        adj_list[b] = {a:True}

visited = {}
print(BFS(N, to_visit, adj_list, visited))
