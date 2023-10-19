# Problem: https://open.kattis.com/problems/flipfive
from collections import deque

# convertToStr: A function that converts a grid to str for comparisons (hashing etc)
def convertToStr(grid):
    return "".join(grid[0]) + "".join(grid[1]) + "".join(grid[2])

# transform: A function that takes in a grid and returns a transformation step (r,c) applied on it
def transform(grid,r,c):

    # 1. Create a new grid and iterate over every row, adding elements to a innerRow variable:
    newGrid = []
    for rowIndex in range(len(grid)):
        newRow = []

        # 2. Iterate over every column value as well:
        for colIndex in range(len(grid[0])):

            # 3. If the manhattan distance is 1 or 0 to a specified tile, then flip it and add the flip to the row:
            if (abs(rowIndex-r) + abs(colIndex-c)) in [1,0]:
                if grid[rowIndex][colIndex] == ".":
                    newRow.append("*")
                else:
                    newRow.append(".")

            # 4. Else, append the old tiles to the new row:
            else:
                newRow.append(grid[rowIndex][colIndex])
        
        # 5. Append a new row:
        newGrid.append(newRow)

    # 6. Return the new grid
    return newGrid

# BFS: A function that performs transformation on BFS to exhaustively try every move.
def BFS(grid):

    # 1. Create datastructures to do a BFS and to make sure we do not come back to already visited tile-constellations:
    toVisit = deque([[grid, 0]])
    visited = {}
    while(len(toVisit) > 0):
        # 2. For as long as we can, extract the current grid and depth:
        currentPackage = toVisit.popleft()
        currentGrid = currentPackage[0]
        currentDepth = currentPackage[1]

        # 3. If the current grid is correct, return it. Else continue:
        if checkDone(currentGrid):
            return currentDepth
        else:
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    newGrid = transform(currentGrid, r, c)
                    if convertToStr(newGrid) not in visited:
                        visited[convertToStr(newGrid)] = True
                        toVisit.append([newGrid, currentDepth+1])

# checkDone: A function that checks if the passed in grid is the correct one by assuming it is and then attemtping to disprove that assumption.
def checkDone(grid):
    for row in grid:
        if not(row[0] == "." and row[1] == "." and row[2] == "."):
            return False
    return True

# Driver code:
if __name__ == "__main__":
    # 0. Tests:
    test = True
    if test:
        inGrid = [list("*.."),list("**."),list("*..")]
        outGrid = transform(inGrid, 1, 0)
        assert (convertToStr(outGrid) == "."*9)

    # 1. Iterate over how many testcases N we have and initiate a grid:
    N = int(input())
    for _ in range(N):
        grid = []
        for _ in range(3):
            grid.append(list(input()))

        # 2. Print the smallest amount of moves found by the BFS:
        print(BFS(grid))
