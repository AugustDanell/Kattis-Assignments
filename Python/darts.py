# Assignment: https://open.kattis.com/problems/dartscores?editsubmit=10659823

# I realized this assignment was similar to one I solved in Haskell for a lab: 
# https://open.kattis.com/problems/calculatingdartscores
# Solution: https://github.com/AugustDanell/Kattis-Assignments/blob/master/Haskell/calculatingDartScores.hs

import math

testcases = int(input())
circles = [i for i in range(20, 220, 20)]

for i in range(testcases):
    totalScore = 0
    throws = int(input())

    for j in range(throws):
        x,y = list(map(int,input().split()))
        r = math.sqrt(x**2 + y** 2)
        points = 10

        for circle in circles:
            if r <= circle:
                totalScore += points
                break
            else:
                points -= 1

    print(totalScore)
