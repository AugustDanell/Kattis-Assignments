# My 678th Kattis. A solution to the problem: https://open.kattis.com/problems/safe

''' General Solution Idea:
    We are essentially doing a BFS. We are trying pressing every button. If we come to
    a constellation that we have visited our get_hash() and visited will take care of that.
    Get hash transforms a grid into a string that can be hashed in the dictionary visited.
    If the hash is not in visited we append it to our list of constellations to visit.
    We use a function called isUnlocked() to check the current grid if we have reached our
    target. get_new_map generates new grids for every current one we have.
'''


from collections import deque
def test_print(grid, i):
    print("Grid {0}:". format(i))
    for row in grid:
        print(row)

def isUnlocked(grid):
    for row in grid:
        for element in row:
            if not element == 0:
                return False
    return True

def get_hash(grid):
    l = []
    for row in grid:
        for element in row:
            l.append(str(element))
    return "".join(l)

def get_new_map(grid, r,c):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[0])):
            if (i == r) or j == c:
                new_row.append((grid[i][j] + 1) % 4)
            else:
                new_row.append((grid[i][j]))
        new_grid.append(new_row)
    return new_grid

grid = []
for _ in range(3):
    grid.append(list(map(int,input().split())))

to_visit = deque([[grid,0]])
visited = {get_hash(grid):True}
found = False

while len(to_visit) > 0:
    current_node = to_visit.popleft()
    current_grid, current_depth = current_node


    if isUnlocked(current_grid):
        print(current_depth)
        found = True
        break

    new_maps = []
    for r in range(3):
        for c in range(3):
            new_map = get_new_map(current_grid, r, c)
            new_maps.append(new_map)

    for new_map in new_maps:
        hash = get_hash(new_map)
        if hash in visited:
            continue
        else:
            visited[hash] = True
            to_visit.append([new_map, current_depth+1])

if not found:
    print(-1)
