# 701th Katts. A solution ot the problem: https://open.kattis.com/problems/monopol

''' General Solution: Simulate dices
    What we can do is just simulate two dices d1 and d2. 
    We have a counter for when d1+d2 lands on a dangerous square.
    Then we print this counter divided by the total for the probability. 
'''

N = int(input())
l = list(map(int,input().split()))
s = 0
for d1 in range(1,6+1):
    for d2 in range(1, 6+1):
        if (d1+d2) in l:
            s += 1

print(s / 36)
