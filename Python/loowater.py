# A solution to the problem: https://open.kattis.com/problems/loowater

# 1. This problem requires input until EOF so we import sys to read in line for line until a specific input is made:
import sys
for line in sys.stdin:
    
    # 2. For every line we split and parse unless we recieve the input 0 0, which signals the last test case:
    heads,knights = list(map(int,line.split()))
    if heads == knights == 0:
        break
    
    # 3. We initiate two lists which we append dragon heads and knights to respectively. We then sort the two lists:
    headList = []
    knightList = []
    for i in range(heads):
        headList.append(int(input()))
    headList = list(sorted(headList))

    for j in range(knights):
        knight = int(input())
        knightList.append(knight)
    knightList = list(sorted(knightList))
    
    # 4. We let the lowest knight slay the lowest dragon head and accumulate the cost. If there are no dragonheads left we simply exit:
    cost = 0
    for lowestKnight in knightList:
        if len(headList) == 0:
            break
        else:
            lowestHead = headList[0]

            # 4.1 Lowest knight slays the lowest head:
            if lowestKnight >= lowestHead:
                headList.pop(0)
                cost += lowestKnight
    
    # 5. Finally we can then output the cost if all the heads are slain. If they are not we output that Loowater is doomed:
    if(len(headList) > 0):
        print("Loowater is doomed!")
    else:
        print(cost)
