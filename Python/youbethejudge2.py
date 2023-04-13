# A solution to: https://open.kattis.com/problems/youbethejudge2

def valid_triomino(grid, colors):
    triominos = 0
    taken_colors = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            next_nodes = []
            current = grid[i][j]

            if not i == 0 and grid[i-1][j] == current:
                next_nodes.append([i-1, j])
            if not i == len(grid)-1 and grid[i+1][j] == current:
                next_nodes.append([i+1, j])
            if not j == 0 and grid[i][j-1] == current:
                next_nodes.append([i, j-1])
            if not j == len(grid)-1 and grid[i][j+1] == current:
                next_nodes.append([i, j+1])

            if len(next_nodes) > 2:
                return 0

            if len(next_nodes) == 2:
                A = next_nodes[0]
                B = next_nodes[1]
                if A[0] == B[0] or A[1] == B[1] or current in taken_colors:
                    return 0
                triominos += 1
                taken_colors[current] = True

    return int(triominos == colors)



if __name__ == "__main__":
    n = int(input())
    N = 2**n
    grid = []
    zeros = 0
    for _ in range(N):
        row = list(map(int,input().split()))
        grid.append(row)
        zeros += row.count(0)

    if not zeros == 1:
        print(0)
    else:
        print(valid_triomino(grid, int((4**n)-1)/3))
