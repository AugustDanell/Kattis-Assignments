# Problem Description: https://open.kattis.com/problems/vemkanvinna

''' General Solution
    1. Create the three in row function to verify a winner.
    2. Create a BFS to find how many moves it takes for each player to win.
    3. In the main function, count how many empty spots there are (I.e open moves).
    4. In the main function, declare two flags for each of the players.
    5. If there are twice as many open moves as there are moves to win for Abdullah,
    then set Abdullah's flag to true.
    6. Since Johan starts, we check if there are (<twice as many open moves> -1)
    instead. An example is something like this: (J, A, J, A, J). In this case, even
    though there are 5 open moves, J can still achieve 3 moves (since he starts). 
'''


from collections import deque

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
    toVisit = deque([[grid, 0]])

    while len(toVisit) > 0:
        currentPackage = toVisit.popleft()
        currentGrid, currentStep = currentPackage

        if abdullah and threeInRow(currentGrid) == "O":
            return currentStep
        elif not abdullah and threeInRow(currentGrid) == "X":
            return currentStep
        elif currentStep == 5:
            return -1

        for i in range(3):
            for j in range(3):
                if currentGrid[i][j] == "_":
                    nextGrid = []
                    for r in range(3):
                        row = []
                        for c in range(3):
                            row.append(currentGrid[r][c])
                        nextGrid.append(row)

                    if abdullah:
                        nextGrid[i][j] = "O"
                    else:
                        nextGrid[i][j] = "X"
                    toVisit.append([nextGrid, currentStep + 1])
    return -1

if __name__ == "__main__":
    grid = []
    spots = 0
    for _ in range(3):
        row = input().split()
        grid.append(row)
        spots += row.count("_")


    Abdullah = BFS(grid)
    Johan = BFS(grid, False)
    AFlag = False
    JFlag = False

    if Abdullah != -1 and Abdullah*2 <= spots:
        AFlag = True
    if Johan != -1 and (Johan*2-1) <= spots:
        JFlag = True

    if AFlag and JFlag:
        print("Abdullah och Johan kan vinna")
    elif AFlag:
        print("Abdullah kan vinna")
    elif JFlag:
        print("Johan kan vinna")
    else:
        print("ingen kan vinna")
