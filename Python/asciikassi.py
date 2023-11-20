N = int(input())
topBotRows = "+" + "-"*N + "+"
grid = [topBotRows]
for _ in range(N):
    grid.append("|" + " "*N + "|")
grid.append(topBotRows)

for row in grid:
    print(row)