# 1. Read in input:
n = int(input())
couples = {}
badCouple = []

# 2. Iterate and record which couples are taken, save duplicates to badCouple:
for _ in range(n//2 + 1):
    a,b = list(map(int,input().split()))
    if a in couples:
        badCouple.append((a))
    if b in couples:
        badCouple.append((b))
    couples[a] = True
    couples[b] = True

# 3. Sort the badCouple to make sure that we are printing them in correct order and print:
badCouple.sort()
print(" ".join(list(map(str, badCouple))))
