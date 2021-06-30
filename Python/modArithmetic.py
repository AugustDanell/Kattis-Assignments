import math

def modularDivision(a,b,m):
    y = findInverse2(b,m)
    if(y > 0):
        return (y*a)%m
    else:
        return -1

# Euclidean multiplicative inverse
# From: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def findInverse2(a,m):
    if(math.gcd(a,m) == 1):
        m0 = m
        y = 0
        x = 1

        if (m == 1):
            return 0

        while (a > 1):
            q = a // m
            t = m

            m = a % m
            a = t
            t = y

            y = x - q * y
            x = t

        if (x < 0):
            x = x + m0

        return x

    return -1



def findInverse(a, m):
    if(math.gcd(a,m) == 1):
        a = a%m
        for i in range(1,m):
            c = (a*i)%m
            #print(a, c)
            if(c == 1):
                return i

    return -1

while(1):
    inp = input()
    if(inp == "0 0"):
        break
    data = inp.split()
    mod = int(data[0])
    cases = int(data[1])
    for i in range(cases):
        data = input().split()
        a = int (data[0])
        b = int (data[2])

        # Chain the if-commands
        if(data[1] == "+"):
            print((a + b)%mod)
        elif(data[1] == "-"):
            print((a-b)%mod)
        elif(data[1] == "*"):
            print((a*b)%mod)
        else:
            # Special case:
            print(modularDivision(a,b,mod))
