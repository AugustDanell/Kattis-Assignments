# 704th Kattis solution, solution to the problem: https://open.kattis.com/problems/smallestmultiple


''' General Solution: 
    1. Use a factorization algorithm to find prime factors.
    2. Use a hashmap to store the maximum amount a prime factor has appeared.
    3. Multiply them all together.
'''

import sys

def find_factors(N):
    l = []
    divisor = 2
    while divisor <= N:
        counter = 0
        while N % divisor == 0:
            counter += 1
            N //= divisor
        if counter > 0:
            l.append([divisor, counter])
        divisor += 1

    return l

for line in sys.stdin:
    raw_numbers = list(map(int,line.split()))
    unique_factors = {}
    for number in raw_numbers:
        factors = find_factors(number)
        for factor in factors:
            if factor[0] not in unique_factors or factor[1] > unique_factors[factor[0]]:
                unique_factors[factor[0]] = factor[1]

    acc = 1
    for factor in unique_factors.keys():
        acc *= factor**unique_factors[factor]

    print(acc)
