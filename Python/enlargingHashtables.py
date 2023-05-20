# 673th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/enlarginghashtables

'''
    General Solution:
    The general solution is very easy. Just set P = 2*N+1 and increment P until P is prime, unless N = 0.
    For checking primality we use square_sieves for faster time complexity than naive sieves.
    Straight forward. 
'''

import math
def squares_sieves(N):
    end = int(math.sqrt(N))
    for i in range(2, end+1):
        if N % i == 0:
            return False
    return True

while True:
    N = int(input())
    if N == 0:
        break
    
    P = 2*N + 1
    while not squares_sieves(P):
        P += 1

    if squares_sieves(N):
        print(P)
    else:
        print("{0} ({1} is not prime)".format(P, N))
