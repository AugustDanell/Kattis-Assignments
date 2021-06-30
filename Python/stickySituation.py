def isTriangle(a,b,c):
    if(a +b > c):
        return True

    return False

sticks = int(input())
data = input().split()

triangleList = []

for i in range(sticks):
    triangleList.append(int(data[i]))

triangleList.sort()
pos = False
for i in range(sticks-2):
    a = triangleList[i]
    b = triangleList[i+1]
    c = triangleList[i+2]

    if(isTriangle(a,b,c)):
        pos = True
        break

if(pos):
    print("possible")
else:
    print("impossible")
