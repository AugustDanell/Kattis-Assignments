a,b = list(map(int,input().split()))
for _ in range(a):
    b -= int(input())

if(b < 0):
    print("Neibb")
else:
    print("Jebb")