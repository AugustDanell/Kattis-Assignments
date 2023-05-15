# O(N**2)-brute force approach. We try every busline and test the sum for distinctness with a hashmap:
def brute_force_solution(V, E):
    found_sum = {}
    combinations = []
    for i in range(1, V+1):
        for j in range(1, V+1):
            if i == j:
                continue

            edge_sum = i + j
            if edge_sum in found_sum:
                continue
            else:
                combinations.append([i, j])
                found_sum[edge_sum] = True
                if len(combinations) == E:
                    return combinations

    return combinations
      
if __name__ == "__main__":
    
    # 1. Read in the data, buslines will be the valid buslines we can have:
    V,E = list(map(int,input().split()))
    buslines = brute_force_solution(V, E)
    
    # 2. If we have more nodes than edges we skip, because obviously the graph cannot be connected:
    if (V-1) > E:
        print(-1)
    
    # 3. Also if our greedy, barbarian algorithm did not find enough edges we return -1:
    elif len(buslines) < E:
        print(-1)
        
    # 4. If, however, we did manage to find E distinct buslines, we simply print them out:
    else:
        for busline in buslines:
            print(busline[0], busline[1])
