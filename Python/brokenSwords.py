swords = int(input())
TB = 0
LR = 0
for i in range(swords):
    swordData = list (input())
    #print(swordData)
    if(swordData[0] == "0"):
        TB += 1
    if(swordData[1] == "0"):
        TB += 1
    if(swordData[2] == "0"):
        LR += 1
    if(swordData[3] == "0"):
        LR += 1

#print(TB, LR)
m = min(TB,LR)
combs = (m//2)
TB -= combs*2
LR -= combs*2

print(combs, TB, LR)