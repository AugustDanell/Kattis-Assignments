sunYears, sunTime = list(map(int, input().split()))
moonYears, moonTime = list(map(int, input().split()))
yearCounter = 0

while not (sunYears == 0 and moonYears == 0):
    sunYears = (sunYears + 1)%sunTime
    moonYears = (moonYears + 1)%moonTime
    yearCounter += 1

print(yearCounter)
