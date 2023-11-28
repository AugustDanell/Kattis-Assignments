# https://open.kattis.com/problems/stadiljus
if __name__ == "__main__":
    N = int(input())
    cost = int(input())
    avg  = int(input())
    lamps = list(map(int, input().split()))
    costPerLamp = map(lambda x: x*cost, lamps)
    sortedLamps = sorted(costPerLamp, reverse=True)
    total = 0
    Y = 0
    while len(sortedLamps) > 0:
        leastCost = sortedLamps.pop()
        currentAvg = (total+leastCost) / (Y+1)
        if currentAvg <= avg:
            total += leastCost
            Y += 1
        else:
            break

    print(Y)
