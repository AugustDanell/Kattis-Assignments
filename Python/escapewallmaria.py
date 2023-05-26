# 690th Kattis. Solution to the problem: https://open.kattis.com/problems/escapewallmaria

''' General Solution: BFS
    We read in the grid and we find our starting position.
    We do a BFS to find any routes to the border of the zone, if there are no such ones we return None.
    Then we just check the time it takes to make this closest traversal. If the time is not
    sufficient (before the titans come) or there are no paths, we output: Impossible.
    Else: output the length of the shortest path. 
'''

from collections import deque
def BFS(start, rows, cols, grid):
    to_visit = deque([[start[0], start[1], 0]])
    visited = {start[0]:{start[1]:True}}

    while len(to_visit) > 0:
        row, col, time = to_visit.popleft()
        if row == 0 or row == rows-1 or col == 0 or col == cols-1:
            return time
        else:
            next_nodes = [[row-1,col], [row+1,col], [row,col-1], [row, col+1]]
            for next_node in next_nodes:
                next_row, next_col = next_node
                access_south = (grid[next_row][next_col] == "U") and next_row > row
                access_north = (grid[next_row][next_col] == "D") and next_row < row
                access_west  = (grid[next_row][next_col] == "L") and next_col > col
                access_east  = (grid[next_row][next_col] == "R") and next_col < col

                if next_row in visited and next_col in visited[next_row] or grid[next_row][next_col] == "1":
                    continue
                elif grid[next_row][next_col] == "0" or access_east or access_west or access_north or access_south:
                    if next_row in visited:
                        visited[next_row][next_col] = True
                    else:
                        visited[next_row] = {next_col:True}

                    next_package = [next_row, next_col, time+1]
                    to_visit.append(next_package)


t,N,M = list(map(int,input().split()))
grid = []
start = -1
for i in range(N):
    row = list(input())
    if "S" in row:
        start = [i, row.index("S")]
    grid.append(row)

earliest = BFS(start, N, M, grid)

if earliest == None or earliest > t:
    print("NOT POSSIBLE")
else:
    print(earliest)
