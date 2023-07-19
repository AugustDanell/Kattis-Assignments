def DFS(start, adj_list):
    to_visit = [[start, 1.0, {}]]
    start_val = 1.0
    visited = {}

    while(len(to_visit) > 0):
        current_package = to_visit.pop()
        current_node = current_package[0]
        current_sum = current_package[1]
        current_dict = current_package[2]

        if current_node == start and len(current_dict) > 0:
            if current_sum < start_val:
                return False
            continue

        if not current_node in adj_list:
            continue
        
        if current_node in visited and visited[current_node] <= current_sum:
            continue
        else:
            visited[current_node] = current_sum

        for next_node in adj_list[current_node].keys():
            if next_node in current_dict:
                continue
            else:
                next_dict = current_dict.copy()
                next_dict[next_node] = visited
                next_sum = current_sum * adj_list[current_node][next_node]
                next_package = [next_node, next_sum, next_dict]
                to_visit.append(next_package)
    return True

while(True):
    n = int(input())
    if n == 0:
        break
    
    V = list(input().split())
    E = int(input())
    ratios = {}
    vertex_map = {}
    for _ in range(E):
        v1,v2,r = input().split(" ")
        if v1 not in vertex_map:
            vertex_map[v1] = True
        if v2 not in vertex_map:
            vertex_map[v2] = True
        
        r1,r2 = list(map(float, r.split(":")))
        if v1 in ratios:
            ratios[v1][v2] = r1/r2
        else:
            ratios[v1] = {v2:r1/r2}
        
    
    ok = True
    for start_vertex in vertex_map.keys():
        if(not DFS(start_vertex, ratios)):
            ok = False
            print("Arbitrage")
            break
    
    if ok:
        print("Ok")
