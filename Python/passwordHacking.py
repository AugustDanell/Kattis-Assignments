numbers = int(input())

exp = 0.
probabilityList = []
for i in range(numbers):
    data = input().split()
    probabilityList.append(float(data[1]))

probabilityList.sort(reverse=True)

for i in range(len(probabilityList)):
    exp = exp +(i+1)*probabilityList[i]

print(exp)

#print(probabilityList)
