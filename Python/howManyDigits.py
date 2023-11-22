# Problem Description: https://open.kattis.com/problems/howmanydigits

''' General Solution
    Use an approximation formula to find how many digits there are approximately.
    (Specialcases inserted so as to manually handle 1 and 0).
'''

import math
import sys

def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return factorial(n-1)*n

def approx(n):
    if n == 0 or n == 1:
        return 1

    return 1 + 1/2*(math.log10(2) + math.log10(math.pi)) + 1/2*(math.log10(n)) + n*(math.log10(n) - math.log10(math.e))


if __name__ == "__main__":
    for line in sys.stdin:
        fac = int(line)
        print(int(approx(fac)))
