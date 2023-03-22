# A generic function we can use to sort on different maps:
def sortOnMap(x, map):
    return map[x]

# 1. Input. Make use of two maps, one that later sorts one that maps starting time and one that maps general time:
runners = int(input())
people = []
nameToGT = {}
nameToST = {}

for _ in range(runners):
    name, start, general = input().split()
    nameToST[name] = float(start)
    nameToGT[name] = float(general)
    people.append(name)

# 2. Define two lambda functions that produces sorted lists based on start or general run time:
sortOnStart = lambda x : sortOnMap(x, nameToST)
sortOnGeneral = lambda x : sortOnMap(x, nameToGT)
startTime = list(sorted(people, key = sortOnStart))
generalTime = list(sorted(people, key = sortOnGeneral))

# 3. Iterate through every start runner and combine it with three general runners. Here is a bottleneck in terms of time complexity but the code is fast enough:
bestTime = 10000000000
bestTeam = []
for startRunner in startTime:
    l = [startRunner]
    for runner in generalTime:
        if startRunner == runner:
            continue
        else:
            l.append(runner)
        if len(l) == 4:
            break
    
    # 4. No need actually for this if statement, but here we process the time of a team. If the team is the best so far we store it as such:
    if len(l) == 4:
        time = nameToST[l[0]]
        for i in range(1, len(l)):
            runner = l[i]
            time += nameToGT[runner]
        if time < bestTime:
            bestTime = time
            bestTeam = l

# 5. Print best time and every member of the best team:
print(bestTime)
for runner in bestTeam:
    print(runner)
