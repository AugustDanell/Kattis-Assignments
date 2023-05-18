# 667th Kattis. A solution to the problem: https://open.kattis.com/problems/brexit

'''
    General solution idea:
    The problem is that we have a network of countries where some countries are trading partners, denoted as an undirected graph.
    If one country leaves the union (starting the reaction) any country with 50% or more of their trading partners left will also
    leave. Will my country leave as part of the "Brexit"?
    
    My solution is to start a BFS which returns False by default and returns True if the BFS at any point reaches my country (target).
    The BFS starts with the country "start" and it adds new countries to a deque each time a country is found where atleast 50% of its
    initial trading partners have left. We use a hashmap -> list to keep track of each countries initial partners and left partners.
'''



from collections import deque

# BFS: The main function of this problem basically:
def BFS(adj_list, neighbor_counter, start, target):
    
    # 1. Initiate a visited hashmap to avoid visiting countries that have already left and a deque for fast BFS:
    to_visit = deque([start])
    visited = {start:True}
    
    # 2. Pop every country in the to_visit deque:
    while len(to_visit) > 0:
        current = to_visit.popleft()
        
        # 3. If the country is our country (the target) return True
        if current == target:
            return True
        
        # 4. Else continue the iteration. If current has neighbours we iterate over each such neighbor as next_node:
        if current not in adj_list:
            continue
        else:
            for next_node in adj_list[current]:
              
                # 5. If next_node is visited, just continue. Else we update its left neighbour counter and we append it to the deque if it is more or equal to 50% of its initial trading partners:
                if next_node in visited:
                    continue
                else:
                    neighbor_counter[next_node][1] += 1
                    if neighbor_counter[next_node][1] / neighbor_counter[next_node][0] >= 0.5:
                        visited[next_node] = True
                        to_visit.append(next_node)
    return False

# 1. Read in data:
V, E, target, start = input().split()
V,E = int(V), int(E)
adj_list = {}
neighbor_counter = {}

# 2. Read in an adjacency list and a counter for initial neighbours:
for _ in range(E):
    a,b = input().split()
    if a in adj_list:
        adj_list[a][b] = True
        neighbor_counter[a][0] += 1
    else:
        adj_list[a] = {b:True}
        neighbor_counter[a] = [1, 0]

    if b in adj_list:
        adj_list[b][a] = True
        neighbor_counter[b][0] += 1
    else:
        adj_list[b] = {a:True}
        neighbor_counter[b] = [1,0]

# 3. Try for the trivial case and if the problem is not trivial then do the BFS:
if target == start:
    print("leave")
else:
    if BFS(adj_list, neighbor_counter, start, target):
        print("leave")
    else:
        print("stay")
