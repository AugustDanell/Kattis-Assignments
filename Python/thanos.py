def naiveCounter(p,g,f):
    i = 0
    while(p <= f):
        p *= g
        i += 1

    print(i)

planets = int(input())
for i in range(planets):
    planetData = input().split()
    population = int(planetData[0])
    growthFactor = int(planetData[1])
    food = int(planetData[2])
    naiveCounter(population,growthFactor,food)


