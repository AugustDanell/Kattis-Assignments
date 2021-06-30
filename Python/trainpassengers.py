inp = input().split()
C = int(inp[0])
n = int(inp[1])
onBoard = 0
possible = True

entered = 0
stayed = 0
for i in range(n):
    inp = input().split()

    left = int(inp[0])
    entered = int(inp[1])
    stayed = int(inp[2])

    onBoard += (entered - left)
    if(onBoard < 0 or onBoard > C):
        #print("p1")
        possible = False
    elif(C > onBoard and stayed > 0):
        #print("p2")
        possible = False



# If passengers after last station still onboard
if(onBoard > 0 or entered > 0 or stayed > 0):
    possible = False

if(possible):
    print("possible")
else:
    print("impossible")