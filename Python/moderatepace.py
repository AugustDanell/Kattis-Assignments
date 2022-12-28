n = int(input())
a1 = input().split()
a2 = input().split()
a3 = input().split()
outlist = []

for i in range(n):
    c1 = int(a1[i])
    c2 = int(a2[i])
    c3 = int(a3[i])

    l = [c1, c2, c3]
    l.sort()
    outlist.append(str(l[1]))

print(" ".join(outlist))
