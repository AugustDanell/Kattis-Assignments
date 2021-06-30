import sys

treeDict = {}
total = 0
for line in sys.stdin:
    #data = line.split()
    line = line[:-1] #Remove newline
    total = total +1
    if(not line in treeDict):
        treeDict[line] = 1
    else:
        treeDict[line] += 1

items = treeDict.items()
sortedTrees = sorted(items)


#print(sortedTrees)
for tup in (sortedTrees):
    print(tup[0], int(tup[1])*100/total)
