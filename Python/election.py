candidates = int(input())

personList = []
voteList = []
partyList = []

for i in range(candidates):
    personList.append(input())
    partyList.append(input())
    voteList.append(0)

votes = int(input())
for i in range(votes):
    vote = input()
    if(personList.__contains__(vote)):
        index = personList.index(vote)
        voteList[index] = voteList[index] + 1

tie = True
max = 0
maxIndex = 0
for i in range(candidates):
    if(voteList[i] > max):
        max = voteList[i]
        tie = False
        maxIndex = i

    elif(voteList[i] == max):
        tie = True

#print(voteList)

if(tie):
    print("tie")
else:
    print(partyList[maxIndex])