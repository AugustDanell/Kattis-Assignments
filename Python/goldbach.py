# Sieves
# We need primes up to 32000.
# We can check numbers up to (32000)^(0.5),
# because if it is not a divisor of one of those numbers it is prime

# Solution to kattis problem "Goldbach's conjecture"

def sieves(n):
    prime = True
    roof = int(n**(0.5))+1
    for i in range(2, roof):
        if(n%i == 0):
            prime = False
            break
    return prime

cases = int(input())
for i in range(cases):

    x = int(input())
    representations = []
    matches = 0

    for j in range(2, (int(x/2) +1)):
        # a + b = x, always.

        a = j
        b = x-j # b > a

        if(sieves(a) and sieves(b)):
            representations.append("%d+%d" % (a,b))
            matches += 1

    print(x, "has",matches,"representation(s)")
    for j in range(matches):
        print(representations[j])

    print()
