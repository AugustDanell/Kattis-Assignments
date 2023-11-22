# Problem Description:
''' General Solution
    1. We can create a tuple of every tower and its occurance, i.e,
    [5, 4] means that a tower of height 4 occurs 4 times.

    2. We can find a bestMin by counting how many deletions of the
    currently highest tower we have done and take that minus the
    second highest tower.

    3. We get a candidate for a min at the end. We print the min
    of how many towers there are or this candidate (since we can
    use vertical removal n times as a worst case).
'''

def createMap(towers):
    tupleMap = {}
    for tower in towers:
        if tower in tupleMap:
            tupleMap[tower] += 1
        else:
            tupleMap[tower] = 1

    tupleList = []
    for tower in tupleMap.keys():
        tupleList.append([tower, tupleMap[tower]])

    return tupleList

if __name__ == "__main__":
    n = int(input())
    data = sorted(list(map(int, input().split())))
    towers = createMap(data)
    globalMin = towers[-1][0]
    deletes = 0

    while len(towers) > 0:
        tower = towers.pop()
        deletes += tower[1]
        if len(towers) > 0:
            localMin = deletes + towers[-1][0]
            if localMin < globalMin:
                globalMin = localMin

    print(min(n, globalMin))
