def fac(n):
    if(n == 1):
        return 1
    else:
        return n*fac(n-1)

e = 1.
n = int(input())

if(n < 15):
    for i in range(n):
        e += 1./fac(i+1)
else:
    e = 2.718281828458995

# Should be accurate enough given problem description

print(e)

