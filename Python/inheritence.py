# 723th Kattis. A Solution To The Problem: https://open.kattis.com/problems/inheritance

''' General Solution: BFS
    1. We feed the target into a BFS
    2. We start with the two starting strings and do every concatenation possible thereafter.
    If a concatenation makes it so we have a number divisible with the target we print it.
    If we "overshoot" we do not append any new strings. 
    (This could be made faster with a simple return most likely)
'''

from collections import deque
def BFS(target):
    visited = {}
    to_visit = deque(["2", "4"])
    while len(to_visit) > 0:
        current = to_visit.popleft()
        number = int(current)
        if number in visited or number > target:
            continue
        else:
            visited[number] = True
            if target % number == 0:
                print(number)
            to_visit.append(current+"2")
            to_visit.append(current+"4")

BFS(int(input()))
