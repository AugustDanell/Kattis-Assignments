## Solution to Character Development

def fac(n):
    if(n == 1):
        return 1
    else:
        return fac(n-1)*n

def combosOf(a,b):
    if(a == b):
        return 1
    else:
        return int(fac(a)/(fac(b)*fac(a-b)))

relationships = int(input())

total = 0
for i in range(2, relationships+1):
    total = total + combosOf(relationships,i)

print(total)