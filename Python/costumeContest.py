def mini(list):
    mini = 1000000
    for i in list:
        if(i < mini):
            mini = i
    return mini

entries = int(input())
costumeList = []
for i in range(entries):
    costume = input()
    costumeList.append(costume)

costumeList.sort()
costumes = []
amount = []

for j in range(entries):
    costume = costumeList.pop(0)
    if(not(costumes.__contains__(costume))):
        costumes.insert(0,costume)
        amount.insert(0,1)
    else:
        index = costumes.index(costume)
        amount[index] = amount[index] +1

costumes.reverse()
amount.reverse()
m = mini(amount)

for i in range(len(costumes)):
    if(m == amount[i]):
        print(costumes[i])
