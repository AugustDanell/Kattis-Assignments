def multAll(l):
    acc = 1
    for element in l:
        acc *= element
    return acc

bestBox = 0
boxes, V = list(map(int,input().split()))
for i in range(boxes):
    v = multAll(list(map(int, input().split())))
    if v > bestBox:
        bestBox = v

print(bestBox-V)
