# 719th Kattis. A solution to the problem: https://open.kattis.com/problems/knightjump

''' General Solution: BFS
    For each position do a BFS to jump to the 8 next positions and if for a certain depth
    we happen to find ourselves on [1,1] (though we use zero-indexing), return the depth
    at that stage.
'''

from collections import deque

def BFS(start, grid):
    to_visit = deque([start])
    visited = {start[0]:{start[1]:True}}
    while len(to_visit) > 0:
        r,c,depth = to_visit.popleft()
        if r == 0 and c == 0:
            return depth

        next_nodes = [[r-1, c+2], [r-1, c-2], [r+1, c+2], [r+1, c-2], [r+2, c-1], [r+2, c+1], [r-2, c-1], [r-2,c+1]]
        for next_node in next_nodes:
            next_r, next_c = next_node
            if next_r >= len(grid) or next_r < 0:
                continue
            elif next_c >= len(grid[0]) or next_c < 0:
                continue
            elif next_r in visited and next_c in visited[next_r]:
                continue
            elif grid[next_r][next_c] == "#":
                continue
            else:
                if next_r in visited:
                    visited[next_r][next_c] = True
                else:
                    visited[next_r] = {next_c:True}
                to_visit.append([next_r, next_c, depth +1])
    return -1

N = int(input())
grid = []
start = []
for row_number in range(N):
    row = list(input())
    if row.__contains__("K"):
        start = [row_number, row.index("K"), 0]
    grid.append(row)

print(BFS(start, grid))
