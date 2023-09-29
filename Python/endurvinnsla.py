cityName = input()
percentage = float(input())
items = int(input())
plastCount = 0
for _ in range(items):
    if(input() == "plast"):
        plastCount += 1

print(["Neibb", "Jebb"][int(percentage  >= (1.0 - (plastCount / items)))])