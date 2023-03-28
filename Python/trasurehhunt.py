# Solution to the problem: https://open.kattis.com/problems/treasurehunt

# 0. Input:
rows,cols = list(map(int,input().split()))
matrix = []
visited = {}
for y in range(rows):
    matrix.append(list(input()))
    visited[y] = {}

x,y = 0,0
moves = 0
while True:
    # 1. Check One, are we out of bounds? 
    if y >= rows or y < 0 or x >= cols or x < 0:
        print("Out")
        break

    # 2. Check Two, have we come back? Going in circles are we?
    if visited[y].__contains__(x):
        print("Lost")
        break
    else:
        visited[y][x] = True

    # 3. Check Three, have we reached our destination? If so, show me your moves:
    if matrix[y][x] == "T":
        print(moves)
        break

    # 4. Check four, can we be moving? If so, move your a$$:
    if matrix[y][x] == "E":
        x+=1
    elif matrix[y][x] == "S":
        y += 1
    elif matrix[y][x] == "W":
        x-=1
    elif matrix[y][x] == "N":
        y -= 1

    moves += 1
