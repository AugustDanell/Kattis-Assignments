# Solution to the problem: https://open.kattis.com/problems/wheresmyinternet

def DFS(adj_list):
    to_visit = [1]
    visited = {1:True}
    while len(to_visit) > 0:
        current = to_visit.pop()
        if not current in adj_list:
            continue
        else:
            for next_node in adj_list[current].keys():
                if not next_node in visited:
                    visited[next_node] = True
                    to_visit.append(next_node)
    return visited

if __name__ == "__main__":
    V,E = list(map(int,input().split()))
    adj_list = {}

    # 1. Create a Undirected Graph:
    for _ in range(E):
        v1,v2 = list(map(int,input().split()))
        if v1 in adj_list:
            adj_list[v1][v2] = True
        else:
            adj_list[v1] = {v2:True}
        if v2 in adj_list:
            adj_list[v2][v1] = True
        else:
            adj_list[v2] = {v1:True}
    
    # 2. Feed the graph to a DFS (or BFS) and start with node 1 and then find a map of all visited nodes:
    visited = DFS(adj_list)

    # 3. If that map has a length of V then output connected (since it is undirected this works). Else just out the unconnected vertices:
    if len(visited) == V:
        print("Connected")
    else:
        for v in range(1, V+1):
            if v not in visited:
                print(v)
