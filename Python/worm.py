inp = input()
split = inp.split()
## Solution to Climbing Worm

a = int(split[0])
b = int(split[1])
h = int(split[2])

current = 0
climbs = 0

while(current < h):
    climbs = climbs + 1
    current = current + a

    if(current < h):
        current = current - b

print(climbs)
