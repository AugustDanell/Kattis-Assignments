n,q = list(map(int, input().split()))
indexMapping = {}
for i in range(n):
    line = input()
    indexMapping[line] = i

for i in range(q):
    query = input().split()
    a,b = query[0], query[1]
    print(abs(indexMapping[a] - indexMapping[b]) - 1)
