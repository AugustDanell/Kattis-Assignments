n, k, d = list(map(int,input().split()))
friends = 0
for _ in range(n):
    friendCanCome = 14 - (d-int(input())) - k <= 0
    if(friendCanCome):
        friends += 1

print(friends)