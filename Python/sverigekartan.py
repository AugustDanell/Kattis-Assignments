# Problem Description: https://open.kattis.com/problems/sverigekartan
''' General Solution
    Basically we have a map of Sweden and we have new islands appearing.
    For the initial map and for each new island we are to print Sweden's
    landmass. 
    
    1. A solution can be to save which coordinates we have visited
    and to do an initial BFS of Stockholm to get the Swedish landmass.
    
    2. For each new island we use the boolean function connectsToSweden().
    If this function returns true we insert the new island as part of the
    BFS, where Sweden's territory is passed as the visited structure. As
    such we never have to recount anything. 
'''

from collections import deque
def BFS(grid, visited, start, rows, cols):
    toVisit = deque([start])
    if start[0] in visited:
        visited[start[0]][start[1]] = True
    else:
        visited[start[0]] = {start[1] : True}

    landmass = 1

    while len(toVisit) > 0:
        currentPackage = toVisit.popleft()
        currentRow, currentCol = currentPackage
        nextNodes = [[currentRow-1, currentCol], [currentRow+1, currentCol], [currentRow, currentCol-1], [currentRow, currentCol+1]]
        for nextNode in nextNodes:
            nextRow, nextCol = nextNode
            if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols:
                continue
            elif nextRow in visited and nextCol in visited[nextRow]:
                continue
            elif grid[nextRow][nextCol] != "#":
                continue
            else:
                if nextRow in visited:
                    visited[nextRow][nextCol] = True
                else:
                    visited[nextRow] = {nextCol: True}

                landmass += 1
                nextPackage = [nextRow, nextCol]
                toVisit.append(nextPackage)
    return landmass

def connectsToSweden(row, col, visited):
    adjNodes = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
    for nextNode in adjNodes:
        nextRow, nextCol = nextNode
        if nextRow in visited and nextCol in visited[nextRow]:
            return True
    return False

if __name__ == "__main__":
    R = int(input())
    C = int(input())
    U = int(input())
    swedishTerritory = {}
    grid = []
    start = []
    for r in range(R):
        row = input()
        if row.__contains__("S"):
            start = [r, row.index("S")]
        grid.append(list(row))
    totalLandmass = BFS(grid, swedishTerritory, start, R, C)
    print(totalLandmass)

    for _ in range(U):
        r,c = list(map(int, input().split()))
        r -= 1
        c -= 1
        grid[r][c] = "#"
        if connectsToSweden(r, c, swedishTerritory):
            start = [r,c]
            totalLandmass += BFS(grid, swedishTerritory, start, R, C)
        print(totalLandmass)
