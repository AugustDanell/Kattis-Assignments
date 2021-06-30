data = input().split()
s = int(data[0])
v1 = int(data[1])
v2 = int(data[2])

m1 = 0
solList = []
while(s >= v1):
    if(s % v2 == 0 or s == 0):
        solList.append([m1,int(s/v2)])

    # Pouring oil into the large bottle:
    m1 += 1
    s -= v1

if(s == 0):
    solList.append([m1,0])
elif(s%v2 == 0):
    solList.append([m1,int(s/v2)])

#print(solList)
#print(s)

if(len(solList) == 0):
    print("Impossible")
else:
    ans = solList[-1]
    print(ans[0], ans[1])