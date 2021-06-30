runners = int(input())
runList = []

minDist = 10**(5)
for i in range(0, runners):
    run = int(input())
    runList.append(run)

for i in range(0, runners):
    dist = runList[i-2] + runList[i]
    if(dist < minDist):
        minDist = dist
    #print(dist, ":", runList[i-2],runList[i])

print(minDist)