# Problem Description: https://open.kattis.com/problems/connectn

''' General Solution:
    One solution to the Connect-N problem is to:
    1. Iterate over every cell in the grid.
    2. For each cell, generate every possible solution:
       Horizontal, Vertical, Left- and Right diagonals
    3. Filter out those that are out of bounds.
    4. Check the remaining valid solutions.
    5. If one solution matches -> Print the player who wins
    6. If, after iteration over every cell, no matches -> Print NONE
'''


def getHorisontalRow(r, c, length):
    row = [[r, c]]
    for i in range(1, length):
        newCell = [r, c + i]
        row.append(newCell)
    return row


assert getHorisontalRow(1, 1, 4) == [[1, 1], [1, 2], [1, 3], [1, 4]]


def getVerticalRow(r, c, length):
    row = [[r, c]]
    for i in range(1, length):
        newCell = [r + i, c]
        row.append(newCell)
    return row


assert getVerticalRow(1, 1, 4) == [[1, 1], [2, 1], [3, 1], [4, 1]]


def getRightDiagonal(r, c, length):
    row = [[r, c]]
    for i in range(1, length):
        newCell = [r + i, c + i]
        row.append(newCell)
    return row


assert getRightDiagonal(1, 1, 4) == [[1, 1], [2, 2], [3, 3], [4, 4]]


def getLeftDiagonal(r, c, length):
    row = [[r, c]]
    for i in range(1, length):
        newCell = [r + i, c - i]
        row.append(newCell)
    return row


assert getLeftDiagonal(0, 3, 4) == [[0, 3], [1, 2], [2, 1], [3, 0]]


def outOfBounds(sequence, r, c):
    for cell in sequence:
        row, col = cell
        if row < 0 or row >= r or col < 0 or col >= c:
            return True
    return False


# Returns the player that wins / None:
def getWin(sequence, grid, N):
    first = grid[sequence[0][0]][sequence[0][1]]
    if first not in ["R", "B"]:
        return None

    counter = 1
    for i in range(1, N):
        nextElement = grid[sequence[i][0]][sequence[i][1]]
        if nextElement == first:
            counter += 1
    if counter == N and (first == "B" or first == "R"):
        return ["BLUE WINS", "RED WINS"][first == "R"]
    return None


if __name__ == "__main__":

    # 1. Initiate the grid:
    grid = []
    r, c, N = list(map(int, input().split()))
    for _ in range(r):
        grid.append(input().split())

    # 2. Iterate over every cell:
    foundSolution = False
    for row in range(r):
        for col in range(c):

            # 3. Get every potential solution:
            s1 = getHorisontalRow(row, col, N)
            s2 = getVerticalRow(row, col, N)
            s3 = getLeftDiagonal(row, col, N)
            s4 = getRightDiagonal(row, col, N)
            allSolutions = [s1, s2, s3, s4]

            # 4. Filter the solutions for out of bounds:
            validSolutions = []
            for solution in allSolutions:
                if not outOfBounds(solution, r, c):
                    validSolutions.append(solution)

            # 5. Test every valid solution:
            for vSolution in validSolutions:
                player = getWin(vSolution, grid, N)
                if player is not None:
                    print(player)
                    foundSolution = True
                    break

            # 6. Break prematurely if solution is found already:
            if foundSolution:
                break
        if foundSolution:
            break

    # 7. If there was no solution, print None:
    if not foundSolution:
        print("NONE")
