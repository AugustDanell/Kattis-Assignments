issues = int(input())
dic = {}

for i in range(issues):
    verdict = input()
    if(dic.__contains__(verdict)):
        dic[verdict] += 1
    else:
        dic[verdict] = 1

maxi = 0
for i in range(issues):
    verdict = input()
    if(dic.__contains__(verdict) and dic[verdict] > 0):
        dic[verdict] -= 1
        maxi += 1

print(maxi)