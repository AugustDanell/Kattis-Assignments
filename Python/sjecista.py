# Kattis Assignment: https://open.kattis.com/problems/sjecista

# The problem is to find the max amount of intersections in a complete graph.
# This is of a combinatorical nature as every 2-pair of edges can form a unique edge and so bin(n,4) is the answer. 
# We can use the binomial coefficient to choose 4 out of n likeso, bin(n,4) = n! / (4! * (n - 4)!

# Standard, recursive definition of factorial: 
def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)

# Input, use the formula above for n > 3 else output 0 since there will be no intersection for complete graphs where V < 3:
n = int(input())
if n <= 3:
    print(0)
else:
    print(fac(n) // (fac(4) * fac(n - 4)))
