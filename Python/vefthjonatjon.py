l = [0, 0, 0]
for _ in range(int(input())):
    line = input().split(" ")
    if(line[0] == "J"):
        l[0] += 1
    if(line[1] == "J"):
        l[1] += 1
    if(line[2] == "J"):
        l[2] += 1

print(min(l))