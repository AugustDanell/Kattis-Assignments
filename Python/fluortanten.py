# Streaming Algorithm. 

# Input and initialize:
children = int(input())
childList = list(map(int,input().split()))
index = 0
bestAcc = 0
currentAcc = 0
totalAcc = 0

# Remove Björn:
childList.remove(0)
children -= 1
bestIndex = len(childList)-1

# Find the value of inserting Björn in the best spot within the queue. 
for i in range(children-1, -1, -1):
    currentAcc += (childList[i])
    totalAcc += childList[i]*(i+1)

    if currentAcc > bestAcc:
        bestAcc = currentAcc
        bestIndex = i

# The best value comes from inserting björn at "bestIndex" and the value is:
print(totalAcc + bestAcc)
