# Solution to the problem: https://open.kattis.com/problems/cyaniderivers

import math

# 1. input:
binaryString = list(input())
counter = 0
maxCounter = 0

# 2. We count the number of occuring ones for O(n). 
for bit in binaryString:
    if bit == "1":
        if counter > maxCounter:
            maxCounter = counter
        counter = 0
    else:
        counter += 1

# 3. The answer will just be the the max occurance rounded upwards:
print(math.ceil(maxCounter/2))
