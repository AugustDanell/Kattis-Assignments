# Problem Description: https://open.kattis.com/problems/gravity


# A DFS algorithm that starts from the floor and marks solid blocks:
def findSolids(grid, rows, cols):
    toVisit = []
    visited = {}
    
    # 1. Mark solid blocks on the floor:
    for col in range(cols):
        if grid[rows-1][col] != " ":
            toVisit.append([rows-1, col])
            if rows-1 in visited:
                visited[rows-1][col] = True
            else:
                visited[rows-1] = {col:True}
    
    # 2. Do a DFS over them to find every solid block:
    while len(toVisit) > 0:
        currentNode = toVisit.pop()
        row, col = currentNode
        candidates = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        validCandidates = []
        for candidate in candidates:
            if 0 <= candidate[0] < rows and 0 <= candidate[1] < cols:
                validCandidates.append(candidate)

        for validCandidate in validCandidates:
            nextRow, nextCol = validCandidate
            if nextRow in visited and nextCol in visited[nextRow]:
                continue

            if grid[nextRow][nextCol] != " ":
                toVisit.append([nextRow, nextCol])
                if nextRow in visited:
                    visited[nextRow][nextCol] = True
                else:
                    visited[nextRow] = {nextCol:True}
    
    # 3. return the solid blocks:
    return visited

if __name__ == "__main__":
    while(True):
        # 1. Input for each test case:
        r,c = list(map(int,input().split()))
        if r == c == 0:
            break
        else:
            
            # 2. Create the initial grid:
            grid = []
            for _ in range(r):
                grid.append(list(input()))
                
            # 3. Iterate for as long as the grid can change:
            while(True):
                
                # 4. Get the solid blocks for this iteration:
                solidBlocks = findSolids(grid, r, c)

                # 5. Deep copy the contents into a temporary list:
                nextList = []
                for row in grid:
                    newRow = []
                    for character in row:
                        newRow.append(character)
                    nextList.append(newRow)

                # 6. Initi a boolean for changes and a list to avoid overwriting drops:
                change = False
                skipList = {}
                
                 # 7. Iterate over every cell and check if a change is made:
                for row in range(r):
                    for col in range(c):
                        
                        # 8. Continue if the cell is irrellevant
                        if grid[row][col] == " ":
                            continue
                        if row in solidBlocks and col in solidBlocks[row]:
                            continue

                        # 9. Fall the piece one step:
                        change = True
                        nextList[row+1][col] = grid[row][col]
                        
                        # 10. Add the piece to the skip list:
                        if row+1 in skipList:
                            skipList[row+1][col] = True
                        else:
                            skipList[row+1] = {col:True}
                        
                        # 11. If (row, col) isn't a new piece in skiplist, write " " there:
                        if row in skipList and col in skipList[row]:
                            continue
                        nextList[row][col] = " "

                # 12. Deep copy content of the new list:
                for row in range(r):
                    for col in range(c):
                        grid[row][col] = nextList[row][col]

                # 13. If no changes have happened then break:
                if not change:
                    break
                
            # 14. Print the final grid:
            for row in grid:
                print("".join(row))
            print()
