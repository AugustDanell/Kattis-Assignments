# Find all primes except the last one
# We know that the prime can be up to 10**9 but we only need to search
# for values up to 10**5, the number x needs atleast 2 divisors and if
# it has no divisors below 10**(4.5) it cannot have two divisors

def findPrimes(n):
    l = []
    i = 2
    while(i < n):
        if(i == 10**(5) and len(l) == 0):
            break

        if(n%i == 0):
            n = n/i
            l.append(i)
        else:
            i = i+1
    return l

n = int(input())
l = findPrimes(n)
#print(findPrimes(20))

print(len(l) + 1)