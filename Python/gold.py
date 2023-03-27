# A solution to the problem: https://open.kattis.com/problems/gold

# An iterative BFS where we pick up coins and stop if we can feel an adjacent trap to play the game "safely" as per the instructions:
def BFS(start_x, start_y, grid, visited):
  
    # 1. Initiate counters, to visit is a list that stores the next traversals in the map:
    totalCoins = 0
    toVisit = [[start_x, start_y]]

    # 2. Iterate over every element in toVisit and extract x and y.
    while len(toVisit) > 0:
        x,y = toVisit.pop(0)

        # 3. If the x and y has already been visited, continue. Else just mark them as visited:
        if visited[y].__contains__(x):
            continue
        visited[y][x] = True

        # 4. If we are standing on a gold coin, increment the total coings:
        if grid[y][x] == "G":
            totalCoins += 1
        
        # 5. Initiate a new movements list and a safe boolean. If it is safe to continue from (x,y), new movements will contains new coordinates for "toVisit":
        new_movements = []
        safe = True

        # 6. Iterate over every new x-coordinate. If it is an unsafe square we set the boolean safe to be False. Else we walk to the new square if its not a wall:
        for x_next in [x-1, x+1]:
            if visited[y].__contains__(x_next):
                continue
            elif grid[y][x_next] in [".", "G"]:
                new_movements.append([x_next, y])
            elif grid[y][x_next] == "T":
                safe = False
        
        # 7. Ditto, but for new y-coordinates:
        for y_next in [y-1, y+1]:
            if visited[y_next].__contains__(x):
                continue
            elif grid[y_next][x] in [".", "G"]:
                new_movements.append([x, y_next])
            elif grid[y_next][x] == "T":
                safe = False

        # 8. If it is safe, we append the contents of new_movements to be visited next:
        if safe:
            for new_movement in new_movements:
                toVisit.append(new_movement)
    
    # 9. Print all the coins we have come accros so far: 
    print(totalCoins)

# 1. Input and init of a visit hashmap:
cols,rows = list(map(int,input().split()))
grid = []
visited = {}
for i in range(rows):
    grid.append(list(input()))
    visited[i] = {}

# 2. Search for the player. When the player is found initiate the BFS:
found_player = False
for x in range(1, cols):
    for y in range(1, rows):
        if grid[y][x] == "P":
            
            # 3. BFS function will beform a BFS search for gold coins in the game and print the total. See BFS():
            BFS(x,y, grid, visited)
            found_player = True
            break
    if found_player:
        break
