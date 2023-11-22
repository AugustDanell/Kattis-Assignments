def threeInRow(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != "_":
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != "_":
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != "_":
        return grid[2][0]
    if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != "_":
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != "_":
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != "_":
        return grid[0][2]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "_":
        return grid[0][0]
    if grid[2][0] == grid[1][1] == grid[0][2] and grid[2][0] != "_":
        return grid[2][0]

def BFS(grid, abdullah=True):
    pass

if __name__ == "__main__":
    grid = []
    for _ in range(3):
        grid.append(input().split())

    ans = threeInRow(grid)
    if ans == "X":
        print("Johan har vunnit")
    elif ans == "O":
        print("Abdullah har vunnit")
    else:
        print("Ingen har vunnit")
