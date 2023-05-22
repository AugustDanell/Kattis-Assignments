# My 680th Kattis. A solution to the problem: https://open.kattis.com/problems/olderbrother

''' General Solution:
    Find a prime divisor P and test if it is the only divisor. Very Straight Forward. 
'''

import math
def find_p(N):
    if N == 1:
        return -1

    for p in range(2, int(math.sqrt(N)) + 1):
        if N%p == 0:
            return p
    return N

N = int(input())
P = find_p(N)
if P == -1:
    print("no")
else:
    while(N%P == 0):
        N //= P
    if N == 1:
        print("yes")
    else:
        print("no")
