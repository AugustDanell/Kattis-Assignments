# My 676th Kattis. Solution to the problem: https://open.kattis.com/problems/elevatortrouble
'''
    General Solution: 
    Just do a BFS on how to press buttons and encapsulate the current dept for each node.
    Straight Forward. 
'''

from collections import deque

f, s, g, u, d = list(map(int,input().split()))
to_visit = deque([[s, 0]])
visited = {s:True}
found_floor = -1

while len(to_visit) > 0:
    current_node = to_visit.popleft()
    current_floor, current_depth = current_node
    if current_floor == g:
        found_floor = current_depth
        break

    UP = current_floor + u
    DOWN = current_floor - d
    if UP <= f and UP not in visited:
        visited[UP] = True
        to_visit.append([UP, current_depth+1])
        
    if DOWN >= 1 and DOWN not in visited:
        visited[DOWN] = True
        to_visit.append([DOWN, current_depth+1])

if found_floor == -1:
    print("use the stairs")
else:
    print(found_floor)
