# 681th Kattis. A solution to the problem: https://open.kattis.com/problems/beautifulprimes

''' General Solution:
    The general solution is this.
    1. Initialize a list of primes where we have a range such that every multiplication of a digit in the upper
    section of the list will 100% create a new digit whereas the lower ones may not.
    2. Initiate a product and run through the list of primes to find a candidate to multiplicate with. If one 
    is found then append it to a list of primes.
    3. Output the list of primes.
'''

tests = int(input())
list_of_primes = [2,3,5,7,11,13]

for _ in range(tests):
    N = int(input())
    l = ["7"]
    product = 7
    iterations = N-1
    eleven = True
    for i in range(iterations):
        digits = 10**(i+1)
        for candidate in list_of_primes:
            if product*candidate >= digits:
                product *= candidate
                l.append(str(candidate))
                break

    print(" ".join(l))
