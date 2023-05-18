# 669th Kattis Solution. Solution to the problem: https://open.kattis.com/problems/grid

from collections import deque

''' General Solution:
    1. Initiate the grid and then put the grid into a BFS.
    2. The BFS will check for a solution and then return the depth of that solution.
    3. If no solution is found BFS simply returns -1. Whatever it returns we print that.
'''


def BFS(n, m, grid):
  
    # 1. Intialize the structures for bookkeeping visited nodes and nodes to visit. Use Deque for constant pop time without refactoring the entire list:
    to_visit = deque([[0, 0, 0]])
    visited = {0:{0:True}}
    
    # 2. For as long as we have nodes to visit, keep visiting them:
    while len(to_visit) > 0:
      
        # 3. Extract the data from the current node:
        current_node = to_visit.popleft()
        row = current_node[0]
        col = current_node[1]
        depth = current_node[2]
        
        # 4. If the node is our target, return it:
        if row == n-1 and col == m-1:
            return depth
        else:
          
            # 5. Else continue iterating by appending the jump to our next nodes:
            jump = grid[row][col]
            next_nodes = [[row + jump, col], [row - jump, col], [row, col + jump], [row, col - jump]]
            
            # 6. Iterate over every next node and see if a jump gets you out of bounds or if we jump to an already visited node:
            for next_node in next_nodes:
                new_row, new_col = next_node
                if (new_row < 0 or new_row >= n) or (new_col < 0 or new_col >= m) or (new_row in visited and new_col in visited[new_row]):
                    continue
                else:
                    
                    # 7. If the logic check in 6. is valid, we append our new node with an updated depth and set its visited status to be true:
                    to_visit.append([new_row, new_col, depth+1])
                    if new_row in visited:
                        visited[new_row][new_col] = True
                    else:
                        visited[new_row] = {new_col:True}
    
    # 8. If we have iterated without finding the target we return -1:
    return -1

# 1. Read in the data:
n,m = list(map(int,input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int,list(input()))))

# 2. Output the result of the BFS:
print(BFS(n, m, grid))
