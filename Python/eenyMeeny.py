inp = input()
split = inp.split()
skipper = len(split) -1

children = int(input())

teamA = []
teamB = []
pool = []
teamASelects = True
for i in range(children):
    pool.append(input())

pointer = 0

while(not(pool == [])):
    mod = len(pool)
    pointer = (pointer + skipper) % mod
    if(teamASelects):
        teamA.append(pool.pop(pointer))
        teamASelects = False
    else:
        teamB.append(pool.pop(pointer))
        teamASelects = True
    pointer = (pointer) % (mod)

print(len(teamA))
for a in teamA:
    print(a)

print(len(teamB))
for b in teamB:
    print(b)