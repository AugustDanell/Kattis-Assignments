#tornbygge
bricks = int(input())
towers = 0
prev = -1 # Will start with the first base, regardless of width.
brickData = input().split()

for i in brickData:
    x = int(i)
    if(prev < x):
        towers += 1

    #print(prev, x)
    prev = x


print(towers)