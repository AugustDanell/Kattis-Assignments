cases = int(input())

for i in range(cases):
    s = input()
    split = s.split()
    N = int(split[0])

    sum = 0
    for j in range(1,N+1):
        sum += int(split[j])

    print(sum - (N-1))