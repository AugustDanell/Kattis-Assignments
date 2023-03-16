# Solution to this Problem: https://open.kattis.com/problems/amoebas

# A recursive function that takes in the coordinates of an amoeba and removes its body with a recursive check:
def recursivelyMarkRest(l, x, y, rows, cols):
  
    # 0. Start with just unmarking our current coordinates in the list, so as to avoid infinite recursion.
    l[y][x] = "."
    
    # 1. Let nextX and nextY be list of potential next coordinates, that 
    nextX = [x]
    nextY = [y]

    # 2. Border check to fill nextX and nextY:
    if (x-1) >= 0:
        nextX.append((x-1))
    if (x+1) < cols:
        nextX.append((x+1))
    if(y-1) >= 0:
        nextY.append((y-1))
    if (y+1) < rows:
        nextY.append((y+1))
    
    # 3. Recurse unto every combination of nextX and nextY provided that they are part of the Amoeba:
    for x1 in nextX:
        for y1 in nextY:
            if l[y1][x1] == "#":
                recursivelyMarkRest(l, x1, y1, rows, cols)


# A) Input:
rows, cols = list(map(int,input().split()))
l = []
for i in range(rows):
    l.append(list(input()))

# B) Look for the start of an amoeba, if found, increment the counter and apply the recursive function for its removal:
amoebas = 0
for y in range(len(l)):
    for x in range(len(l[y])):
        if l[y][x] == "#":
            recursivelyMarkRest(l, x, y, rows, cols)
            amoebas += 1

print(amoebas)
