N = int(input())
list = []

for i in range(N):
    list.append(int(input()))

for i in range(N-1,-1,-1):
    print(list[i])