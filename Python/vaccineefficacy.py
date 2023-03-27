# A solution to the problem: https://open.kattis.com/problems/vaccineefficacy

# 1. Input. Initiate the control group and study group:
participants = int(input())
controlGroup = [0,0,0,0]
studyGroup = [0,0,0,0]
for _ in range(participants):
    # 2. Use a simple lambda function to convert "Y" to 1 and "N" to 0:
    f = lambda x : 1 if x == "Y" else 0

    g,a,b,c = list(input())
    a,b,c = list(map(f, [a,b,c]))
    
    # 3. For every participant, check which group they are in and increment strains for which they have a "Y":
    if g == "N":
        controlGroup[0] += 1
        controlGroup[1] += a
        controlGroup[2] += b
        controlGroup[3] += c
    else:
        studyGroup[0] += 1
        studyGroup[1] += a
        studyGroup[2] += b
        studyGroup[3] += c

# 4. Print out percentages where the vaccince was effective:
aC = controlGroup[1]/controlGroup[0]
aS = studyGroup[1]/studyGroup[0]
if aS < aC:
    print((1.0 - (aS/aC))*100)
else:
    print("Not Effective")

bC = controlGroup[2]/controlGroup[0]
bS = studyGroup[2]/studyGroup[0]
if bS < bC:
    print((1.0 - (bS/bC))*100)
else:
    print("Not Effective")

cC = controlGroup[3]/controlGroup[0]
cS = studyGroup[3]/studyGroup[0]
if cS < cC:
    print((1.0 - (cS/cC))*100)
else:
    print("Not Effective")
