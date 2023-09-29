n = int(input())
total = 0
possibleFlag = True
for _ in range(n):
    a,b = list(map(int, input().split()))
    total += a
    if(total < b):
        possibleFlag = False
        print("impossible")
        break

if(possibleFlag):
    print("possible")