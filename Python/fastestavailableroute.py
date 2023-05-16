# 662th Solution. A BFS solution to the problem

'''
General Solution:
We import a deque for constant time removal of the first element without having to shift the remainder of the list.
We then employ a BFS search for the target. In each node we encapsulate the level of the BFS. When the target is found
we simply return that depth.
'''

from collections import deque

# A helper function to get the neighboring nodes from East, West, North and South:
def get_neighbours(row, col, row_max, col_max):
    l = []
    for new_row in [row-1, row +1]:
        if new_row < 0 or new_row >= row_max:
            continue
        new_node = [new_row, col]
        l.append(new_node)

    for new_col in [col-1, col+1]:
        if new_col < 0 or new_col >= col_max:
            continue
        new_node = [row, new_col]
        l.append(new_node)

    return l

# The function that executes the search. Use a deque for faster BFS and the usual queue structure for BFS:
def BFS(start, grid, row_max, col_max):
  
    # 1. Initialize the starting values:
    start_row = start[0]
    start_col = start[1]
    start_level = 0
    to_visit = deque([[start_row, start_col, start_level]])
    visited = {start_row:{start_col:True}}
    
    # 2. For as long as we have nodes to visit, empty the queue of nodes:
    while len(to_visit) > 0:
      
        # 3. Unpack the current node, get its row and col number and depth:
        current_node = to_visit.popleft()
        current_row = current_node[0]
        current_col = current_node[1]
        current_lvl = current_node[2]
        
        # 4. Check if we have reached our target, if so, just return the current depth:
        if grid[current_row][current_col] == "$":
            return current_lvl
        
        # 5. Else, iterate over a list of neighbors, call each neighbor next_node:
        next_nodes = get_neighbours(current_row, current_col, row_max, col_max)
        for next_node in next_nodes:
            
            # 6. Unpack next_node:
            next_row = next_node[0]
            next_col = next_node[1]
            
            # 7. Check if the tuple (r,c) has already been visited, if so, skip this node:
            if next_row in visited and next_col in visited[next_row]:
                continue
                
            # 8. Else, check if it is a traversable path or the target. If so, mark the node as visited and append it with an updated level of depth:
            elif grid[next_row][next_col] in [".", "$"]:
                if next_row in visited:
                    visited[next_row][next_col] = True
                else:
                    visited[next_row] = {next_col:True}
                next_node.append(current_lvl+1)
                to_visit.append(next_node)

# 1. Read in the initial data and initialize starting positions and grid:
h,w,s = list(map(int,input().split()))
grid = []
start = []
for row_number in range(h):
    row = list(input())
    if row.__contains__("@"):
        start = [row_number, row.index("@")]
    grid.append(row)

# 2. Calculate the distance and output it with the scalar s:
distance = BFS(start, grid, h, w)
print("Your destination will arrive in {0} meters".format(s*distance))
