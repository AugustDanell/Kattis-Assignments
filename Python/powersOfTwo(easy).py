n,e = list(map(int,input().split()))
match_str = str(2**e)
count = 0
for i in range(0, n+1):
    s = str(i)
    if match_str in s:
        count +=1

print(count)
