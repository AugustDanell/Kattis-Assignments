# 722th Kattis, A Solution To The Problem: https://open.kattis.com/problems/amsterdamdistance

''' General Solution: Brute Force
    What we can do is to walk to the smallest of the two y coordinates, we call each step 
    towards the center of the circle / circumference a y_step. We then try to walk towards
    the center and for each such step we record the distance it would take to move in the
    x direction. This gives us a list. From that list we output the minimum distance. 
'''

import math
def x_step(radius, M):
    return math.pi*radius/M

M,N,R = input().split()
M = int(M)
N = int(N)
R = float(R)
y_step = R/N
x1,y1,x2,y2 = list(map(int,input().split()))
dist = abs(y1-y2)*y_step
dist_list = []
y = min(y1,y2)
steps = 0
while y >= 0:
    current_radius = R * y / N
    dist_list.append(dist + 2*steps*y_step + abs(x1-x2)*x_step(current_radius, M))
    steps += 1
    y-=1

print(min(dist_list))
