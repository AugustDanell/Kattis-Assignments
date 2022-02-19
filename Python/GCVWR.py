a,b,c = list(map(int,input().split()))
d = (a - b)*0.9

print(int(d - sum(list(map(int,input().split())))))
