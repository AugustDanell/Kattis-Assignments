# A solution to the problem: https://open.kattis.com/problems/slikar

'''
    Spreading Algorithm
    The solution is an algorithm that spreads to neighbouring tiles, like a "game of life" of sorts. The player will spread S on the map and the floods
    will spread * on the map. For each iteration we are iterating over each tile in the map/grid. First priority is another flood tile. If we have 
    a flood tile adjacent to us then our current tile will be marked as B or Y (depending on if the tile is . or S). If we are on a tile marked as "."
    and there is a player square adjacent (either a Y or an S) then this square will become an S as well. (Y stands for player square to be flooeded next).
    So we perform the spreading algorithm in two steps. 1. Mark new squares. 2. Transform them. Iterate over step 1 and 2 till we find a solution or we cant
    move anymore. 
'''

def pretty_print_grid(grid):
    print("Testing Grid:")
    for line in grid:
        print(line)

def spread(max_row, max_col, grid):
    spreads = 0
    
    # 1. Marking Stage
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == "X" or grid[i][j] == "D" or grid[i][j] == "*" or grid[i][j] == "Y" or grid[i][j] == "B":
                continue

            flood_next = False
            player_next = False

            for next_row in [i-1, i+1]:
                if next_row < 0 or next_row >= max_row:
                    continue
                else:
                    if grid[next_row][j] == "D" and (grid[i][j] == "S" or grid[i][j] == "Y"):
                        return 0, 1

                    elif grid[next_row][j] == "*":
                        flood_next = True

                    elif grid[next_row][j] == "S" or grid[next_row][j] == "Y":
                        if grid[i][j] == ".":
                            spreads += 1
                            player_next = True

            for next_col in [j-1, j+1]:
                if next_col < 0 or next_col >= max_col:
                    continue
                else:
                    if grid[i][next_col] == "D" and (grid[i][j] == "S" or grid[i][j] == "Y"):
                        return 0, 1

                    elif grid[i][next_col] == "*":
                        flood_next = True

                    elif grid[i][next_col] == "S" or grid[i][next_col] == "Y":
                        if grid[i][j] == ".":
                            spreads += 1
                            player_next = True

            if player_next:
                grid[i][j] = "N"
            if flood_next:
                if grid[i][j] == "S":
                    grid[i][j] = "Y"
                else:
                    grid[i][j] = "B"

    # 2. Transformation stage:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "N":
                grid[i][j] = "S"
            elif grid[i][j] == "B" or grid[i][j] == "Y":
                grid[i][j] = "*"

    return spreads, -1

if __name__ == "__main__":
    R,C = list(map(int,input().split()))
    grid = []
    for _ in range(R):
        grid.append(list(input()))

    iterations = 0
    flag = -1
    while(True):
        spreads, flag = spread(R,C,grid)
        iterations += 1
        if spreads == 0 or flag == 1:
            break

    if flag == 1:
        print(iterations)
    else:
        print("KAKTUS")
