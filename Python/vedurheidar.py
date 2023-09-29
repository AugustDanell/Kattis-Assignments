speedLimit = int(input())
n = int(input())
cities = []
for _ in range(n):
    city, speed = input().split()
    speed = int(speed)
    if(speed < speedLimit):
        cities.append(city + " lokud")
    else:
        cities.append(city + " opin")

for city in cities:
    print(city)