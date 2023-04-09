# A solution to: https://open.kattis.com/problems/breakingbad
def read_in_data():
    # 1. Read in the Vertices:
    n = int(input())
    items = {}
    for _ in range(n):
        items[input()] = True
    
    # 2. Init adjacency matrix according to an undirected graph and append nodes according to edges. Also return as found_items nodes of degree 0:
    adj_matrix = {}
    found_items = set()
    m = int(input())
    for _ in range(m):
        v1, v2 = input().split()
        found_items.add(v1)
        found_items.add(v2)

        if adj_matrix.__contains__(v1):
            adj_matrix[v1][v2] = True
        else:
            adj_matrix[v1] = {v2: True}

        if adj_matrix.__contains__(v2):
            adj_matrix[v2][v1] = True
        else:
            adj_matrix[v2] = {v1: True}
    
    # 3. Return relevant data:
    return items, adj_matrix, found_items, n


def alternate_path(start_node, Walter, Jesse, adj_matrix):
    # 1. Initiate visited and perform a DFS:
    visited = {}
    to_visit = [[start_node, True]]
    Walter[start_node] = True
    
    # 2. For as long as we have nodes to visit we let current be the node to process:
    while len(to_visit) > 0:
        current = to_visit.pop()
        current_node = current[0]
        to_walter = current[1]
        visited[current_node] = True
        
        # 3. For every current node we extract the neighbours as next_node:
        for next_node in adj_matrix[current_node].keys():
            
            # 4. If next_node is found already we continue:
            if next_node in visited:
                continue
            
            # 5. If the current node is Walter's we assign the next to Jesse and vice versa:
            if to_walter:
                Jesse[next_node] = True
            elif not to_walter:
                Walter[next_node] = True
            
            # 6. However, if the current node is Walter's or Jesse's and the next_node is the same, we return the matching as false and re-set Walter and Jesse:
            if to_walter and next_node in Walter:
                Walter = {}
                Jesse = {}
                return False
            elif not to_walter and next_node in Jesse:
                Walter = {}
                Jesse = {}
                return False
            else:
            # 7. If the next node is valid and not visited we append it to the stack:
                to_visit.append([next_node, not to_walter])


if __name__ == "__main__":
    # 1. Read in Data and initiate maps for Jesse and Walter:
    items, adj_list, taken_items, N = read_in_data()
    Walter = {}
    Jesse = {}
    visited = {}

    # 2. Iterate over each item. If it is an item with degree 0 we assign them to Jesse or Walter without questioning:
    for item in items:
        if item not in taken_items:
            if len(Walter) >= len(Jesse):
                Walter[item] = True
            else:
                Jesse[item] = True
    
    # 3. Iterate over items with a degree > 0. If the item has been matched already in a previous matching ignore it. Else we attempt to find a matching:
    for item in adj_list.keys():
        if item not in Walter and item not in Jesse:
            if item in visited:
                continue
            else:
                # 4. Use an algorithm for alternating paths and unmark all the items we can find on the way:
                match = alternate_path(item, Walter, Jesse, adj_list)
    
    # 5. If we have found all the items in our alternating algorithm we print what we found. Else we print impossible:
    if (len(Walter) + len(Jesse) == N):
        print(" ".join(list(Walter.keys())))
        print(" ".join(list(Jesse.keys())))
    else:
        print("impossible")
