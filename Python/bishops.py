# General Idea:
# 1. Fill up the top row with N bishops, given that they are adjacent they will not threaten each other.
# 2. Fill up the lowest row with bishops where you can. Only the leftmost and the rightmost bishop will be able to traverse from top to down.
# 3. For dimensions greater than 1 this yields the formula: |valid_bishops|= n + (n-2)

import sys
for line in sys.stdin:
    n = int(line)
    if n == 1 or n == 2:
        print(n)
    else:
        print(n + (n-2))
