import math


while True:
    n = int(input())
    if(n == 0):
        break

    totX = 0
    totY = 0
    distance_list = []

    for i in range(n):
        s = input().split()
        x,y = float(s.pop(0)), float(s.pop(0))
        s.pop(0)
        angle = float(s.pop(0))

        while(len(s) > 0):
            instruction = s.pop(0)
            units = float(s.pop(0))

            if(instruction == "turn"):
                angle += units
            else:
                x += math.cos(math.radians(angle))*units
                y += math.sin(math.radians(angle))*units

        distance_list.append([x, y])
        totX += x
        totY += y

    avgX = totX/n
    avgY = totY/n
    worstDist = 0
    dist = 0

    for dest in distance_list:
        dist = math.sqrt(math.pow(avgX - dest[0], 2) + math.pow(avgY - dest[1], 2))
        if(dist > worstDist):
            worstDist = dist

    print(avgX, avgY, worstDist)
