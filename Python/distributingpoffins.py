# A solution to the problem: https://open.kattis.com/problems/distributingpoffins

# Idea: When we redistribute like this (We did it in another problem called cats) we will end up with either a difference of 1 or a difference of 0.
# Just print depending on the remainder of poffins. Make sure to have a bounds check for division with zero.

N,P = list(map(int,input().split()))
if N == 0 or P % N == 0:
    print(0)
else:
    print(1)
