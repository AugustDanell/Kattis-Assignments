# 688th Kattis Solution.

''' General Solution:
    The problem is to take 3 students so as to maximize the median. This can be done easily.
    We just take three students consisting of the best, the second best and the worst.
    We accumulate the score over every such triple and just output it. Easy. 
'''

from collections import deque
cases = int(input())
for _ in range(cases):
    N = 3*int(input())
    team = deque(sorted(list(map(int,input().split())), reverse=True))
    score = 0
    while len(team) > 0:
        team.pop()
        team.popleft()
        score += team.popleft()

    print(score)
