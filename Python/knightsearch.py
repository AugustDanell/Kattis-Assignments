# 727th Kattis, A Solution To the Problem: https://open.kattis.com/problems/knightsearch

''' General Solution: DFS
    Here we can employ either a DFS or a BFS it wouldn't matter really, but a DFS pops from
    the end of the stack and as a result a normal python list does not need to be refactored
    and as such a DFS with a list as a supporting structure is faster than a BFS. The idea is
    simple. We start at every I and then we jump to the next character if the depth of the jump
    matches the item of that string, and we append new coordinates and a new depth. If we reach
    a depth that matches the length of the string -1 (due to zero-indexing) we return True.
'''

# A function that uses a specific start to find a path writing out the message if it exists:
def DFS(start, grid, N):
    to_visit = [[start[0], start[1], 0]]
    str_msg = "ICPCASIASG"
    while len(to_visit) > 0:
        row, col, depth = to_visit.pop()
        if depth == len(str_msg)-1:
            return True
        else:
            vals = [-1, 1, -2, 2]
            next_nodes = []
            for x in vals:
                for y in vals:
                    if x**2 + y**2 == 5:
                        next_nodes.append([row +x, col+y])

            for next_node in next_nodes:
                next_row, next_col = next_node
                if next_row < 0 or next_row >= N:
                    continue
                elif next_col < 0 or next_col >= N:
                    continue
                elif grid[next_row][next_col] == str_msg[depth+1]:
                    to_visit.append([next_row, next_col, depth+1])
    return False

# Read in data:
N = int(input())
s = list(input())
starts = []
grid = []
for row in range(N):
    append_row = []
    for col in range(N):
        append_row.append(s[col + row*N])
        if s[col + row*N] == "I":
            starts.append([row, col])
    grid.append(append_row)

# Test every start:
found = False
for start in starts:
    found = DFS(start, grid, N)
    if found:
        break

# Print the result of what we found:
print(["NO", "YES"][int(found)])
