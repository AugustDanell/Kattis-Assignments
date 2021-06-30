rolls = int(input())
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
six = 0

data = input().split()
for i in range(rolls):
    if(data[i] == "1"):
        ones += 1
    elif(data[i] == "2"):
        twos += 1
    elif(data[i] == "3"):
        threes += 1
    elif(data[i] == "4"):
        fours += 1
    elif(data[i] == "5"):
        fives += 1
    else:
        six += 1

high = 0
l = [ones, twos,threes,fours,fives,six]

for i in range(6):
    if(l[i] == 1):
        high = i+1

if(high > 0):
    high = data.index(high.__str__()) + 1
    print(high)
else:
    print("none")