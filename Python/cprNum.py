cprNum = input()
numList = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
sum = 0

for i in cprNum:
    if(not i == '-'):
        sum += int(i) * numList.pop(0)

if(sum % 11 == 0):
    print(1)
else:
    print(0)
