ticks = int(input())
currentTick = 0
prevTick = 0
time = 0

if ticks % 2 == 1:
    print("still running")
else:
    for i in range(ticks):
        if i % 2 == 0:
            prevTick = int(input()) # Keeping track of the tick

        else:
            time += int(input()) - prevTick

    print(time)