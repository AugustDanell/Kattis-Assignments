grid = []
for _ in range(3):
    grid.append(list(input()))

winFlag = False
for row in range(3):
    for col in range(3):
        winningTrio = [
            [[row-1, col], [row, col], [row+1, col]],
            [[row, col-1], [row, col], [row, col+1]],
            [[row-1, col-1], [row, col], [row+1, col+1]],
            [[row-1, col+1], [row, col], [row+1, col-1]]
        ]
        
        for trio in winningTrio:
            points = 0
            for cell in trio:
                if(cell[0] < 0 or cell[0] > 2 or cell[1] < 0 or cell[1] > 2):
                    continue
                elif grid[cell[0]][cell[1]] == "O":
                    points += 1
            
            if(points == 3):
                winFlag = True
                break

if(winFlag):
    print("Jebb")
else:
    print("Neibb")