cols = int(input())
rows = int(input())
cars = 0
total = 0

for n in range(rows):
    row = list(input())
    cars += row.count("#")
    total += cols

print(1 - (cars / total))