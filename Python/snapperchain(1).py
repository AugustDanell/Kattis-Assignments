cases = int(input())
# Kattis Problem: Snapper Chain Hard.

for i in range(cases):
    data = input().split()
    chain = int(data[0])
    snaps = int(data[1])
    s = 0
    turnaround = 2**(chain)

    for j in range(chain):
        s += 2**(j)

    snaps %= turnaround

    if(snaps == s):
        print("Case #%d: ON" %(i+1))
    else:
        print("Case #%d: OFF" % (i + 1))



