# 712th Kattis, A Solution to The Problem: https://open.kattis.com/problems/missingnumber

''' General Solution: Using a deque to access numbers and match them.
    1. We can read in our numbers into a deque.
    2. We can then pop the front of the deque and see, for example, if we are on number 3
    the deque should pop 3. If we are on number 34 the deque should pop two letters, 3, 4.
    3. If, by this process, the number has not been found yet, we print N.
'''

from collections import deque
N = int(input())
numbers = deque(list(input()))
found = False

for number in range(1,N):
    str_num = str(number)
    l = []
    for _ in range(len(str_num)):
        l.append(numbers.popleft())

    if not str_num == "".join(l):
        print(number)
        found = True
        break

if not found:
    print(N)
