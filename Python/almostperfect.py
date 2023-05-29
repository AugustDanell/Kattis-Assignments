# 697th Kattis, a solution to the problem:

''' General Solution: Find divisors to numbers
    For this problem we should find divisors to a number to see if the number
    is perfect, almost perfect or not perfect. Almost perfect is when the sum
    of the divisors - the number is in the range [-2, 2]. We have a somewhat
    ugly function, but one that is faster than the naive one, to find the
    divisors. We then sum the divisors and output accordingly. Straight forward.
'''

import math
import sys


def find_divisors(N):
    divisors = [1]
    Q = N
    i = 2
    mapping = {}
    while i <= N:
        if N % i == 0:
            new_divisors = []
            for divisor in divisors:
                product = i*divisor
                if product not in mapping and not product == Q:
                    new_divisors.append(product)
                    mapping[product] = True

            divisors += new_divisors
            N //= i
        else:
            i+= 1

    return divisors

for number in sys.stdin:
    N = int(number)
    S = sum(find_divisors(N))
    #print(naive_find_divisors(N))
    if(S == N):
        print("{0} perfect".format(N))
    elif(abs(S-N) <= 2):
        print("{0} almost perfect".format(N))
    else:
        print("{0} not perfect".format(N))
