l1 = list(input())
l2 = list(input())
mergeList = []

while len(l1) > 0 or len(l2) > 0:
    if len(l1) == 0:
        mergeList.append(l2.pop(0))
    elif len(l2) == 0:
        mergeList.append(l1.pop(0))
    else:
        if l1[0] <= l2[0]:
            mergeList.append(l1.pop(0))
        else:
            mergeList.append(l2.pop(0))

print("".join(mergeList))
