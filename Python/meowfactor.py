# Solution to the problem: https://open.kattis.com/problems/meowfactor
n = int(input())
highest = 1
m = 2
d = m**9
while d <= n:
    if n % d == 0:
        highest = m
    m+=1
    d = m**9
print(highest)
