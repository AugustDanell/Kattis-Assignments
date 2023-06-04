# 703th Kattis, solution to the problem: https://open.kattis.com/problems/birthday

''' General Solution: BFS for every removal of an edge a,b = e.
    See if we can visit every node if we remove every edge in the network. 
    If we can, output no.
    If we cant, output yes.
''' 


from collections import deque

def BFS(start, V, a, b, adj_list):
    to_visit = deque([start])
    visited = {start:True}
    while len(to_visit) > 0:
        current = to_visit.popleft()
        if current not in adj_list:
            continue
        for next_node in adj_list[current].keys():
            if next_node in visited or (a == current and next_node == b) or (a == next_node and b == current):
                continue
            else:
                visited[next_node] = True
                to_visit.append(next_node)

    #print(visited, V)
    return not len(visited) == V

while True:
    line = input()
    if line == "0 0":
        break

    V,E = list(map(int, line.split()))

    # 1. Read in an adjacency list:
    adj_list = {}
    for _ in range(E):
        a,b = list(map(int,input().split()))
        if a in adj_list:
            adj_list[a][b] = True
        else:
            adj_list[a] = {b:True}
        if b in adj_list:
            adj_list[b][a] = True
        else:
            adj_list[b] = {a:True}

    # 2. Let every edge e = (a,b) and if the BFS cannot be made then set impossible to be True:
    impossible = False
    for a in range(V):
        if not a in adj_list:
            continue

        for b in adj_list[a].keys():
            if BFS(0, V, a, b, adj_list):
                impossible = True
                break
        if impossible:
            break

    # 3. Handle the special case:
    if V == 1:
        impossible = False

    print(["No", "Yes"][impossible])
