kitten = int(input())    # The branch for which the Kitten is sitting and need be saved.
treeMap = {}

while(True):
    branches = input().split()
    if(branches[0] == "-1"):
        break
    else:
        branch = int(branches[0])
        length = len(branches)
        for i in range(1, length):
            treeMap[int(branches[i])] = branch

## Tree Map should now be populated:
#print(treeMap) # Ok!

s = [kitten.__str__()]
# Now we traverse the tree:
while(True):
    if(treeMap.__contains__(kitten)):
        kitten = treeMap[kitten]
        s.append(kitten.__str__())

    else:
        break

for i in s:
    print(i, end = " ")
