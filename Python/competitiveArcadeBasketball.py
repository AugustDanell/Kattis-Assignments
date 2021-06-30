data = input().split()
participants = int(data[0])
goal = int(data[1])
shots = int(data[2])
noWinners = True

winList = []
participantDic = {}
for i in range(participants):
    participantDic[input()] = 0

for i in range(shots):

    data2 = input().split()
    name = data2[0]
    score = int(data2[1])
    if(winList.__contains__(name)):
        continue

    participantDic[name] += score
    #print(participantDic[name])
    if(participantDic[name] >= goal):
        winList.append(name)
        noWinners = False

if(noWinners):
    print("No winner!")
else:
    for i in range(len(winList)):
        print(winList[i], "wins!")