inp = input()
split = inp.split()

n = int(split[0])
budget = int(split[1])
hotels = int(split[2])
weeks = int(split[3])

totalCost = 0
worksOut = True
weekList = []
priceList = []
min = budget + 1

for i in range(hotels):
    priceList.append(int(input()))
    availableBeds = (input())
    weekList.append(availableBeds.split())

for i in range (weeks):
    for h in range(hotels):
        bedsHere = int((weekList[h])[i])
        if(n <= bedsHere and priceList[h] < min):
            min = priceList[h]

totalCost = n*min
if(totalCost <= budget):
    print(totalCost)
else:
    print("stay home")