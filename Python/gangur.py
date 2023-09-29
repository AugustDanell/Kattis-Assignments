line = list(input())
leftGoing = 0
leftHash = {}
for index in range(len(line)):
    if(line[index] == "<"):
        leftGoing += 1
    leftHash[index] = leftGoing
    
totalPasses = 0
for index in range(len(line)):
    letter = line[index]
    if(letter == ">"):
        totalPasses += leftGoing - leftHash[index]
        
print(totalPasses)