# Kattis Assignment: https://open.kattis.com/problems/huntthewumpus

import math
import sys

# Take a seed and alter it depending on the formula and extract the coordinates (x,y), return (s',x,y), where s' is the new seed:
def generateCoordinates(seed):
    seed = seed + math.floor(seed / 13) + 15 % 100
    x = (seed % 100) // 10
    y = seed % 10
    return seed, x, y

# Find the closest neighbor based on the manhattan distance norm:
def findClosestManhattan(l,x,y):
    closestDistance = -1
    for wumpus in l:
        x1,y1 = wumpus
        if closestDistance == -1:
            closestDistance = abs(x1-x) + abs(y1-y)
        elif abs(x1-x) + abs(y1-y) < closestDistance:
            closestDistance = abs(x1-x) + abs(y1-y)

    return closestDistance

# A function that pops a member of the list if it collides with (x,y) and then returns the bool value of a hit:
def checkForHit(l,x,y):
    remove = False
    index = 0
    for wumpus in l:
        x1,y1 = wumpus
        if x1 == x and y1 == y:
            remove = True
            break
        else:
            index += 1

    if remove:
        l.pop(index)
        return True
    return False

# 1. Generate the initial seed and coordinates
s,x,y = generateCoordinates(int(input()))
l = [[x,y]]

# 2. Generate the other 3 Wumpus based on Seed:
for i in range(3):
    while True:
        s,x,y = generateCoordinates(s)

        # Check if coordinates already exists:
        foundSame = False
        for wumpus in l:
            x1,y1 = wumpus
            
            # If they exist, mark the flag and break the loop:
            if x1 == x and y1 == y:
                foundSame = True
                break
        
        # Append a new set of coordinates to l:
        if not foundSame:
            l.append([x,y])
            break

# 3. User Inputs:
moves = 0
for line in sys.stdin:
    coordinateData = line.strip()
    x,y = map(int,list(coordinateData))

    if checkForHit(l, x, y):
        print("You hit a wumpus!")

    moves += 1
    if len(l) > 0:
        print(findClosestManhattan(l, x, y))
    else:
        break

# 4. Kattis Output for the assignment:
print("Your score is {0} moves.".format(moves))
