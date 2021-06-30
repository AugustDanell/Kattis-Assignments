testcases = int(input())

for i in range(testcases):
    dim = int(input())
    v1 = input().split()
    v2 = input().split()

    l1 = []
    l2 = []
    for j in range(dim):
        l1.append(int(v1[j]))
        l2.append(int(v2[j]))

    minSum = 0
    l1.sort()
    #print(l1)
    l2.sort(reverse=True)
    #print(l2)

    for j in range(dim):
        minSum += l1[j]*l2[j]

    print("Case #%d: %d" %((i+1), minSum))