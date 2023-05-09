# A solution to the problem: https://open.kattis.com/problems/excursion

queue = input()
zeros = 0
ones = 0
twos = 0
swaps = 0

# 1. Push the zeroes first:
zero_counter = 0
for c in queue:
    if c == "0":
        swaps += zero_counter
    else:
        zero_counter += 1

# 2. Push the ones to the center:
one_counter = 0
for c in queue:
    if c == "0":
        continue
    elif c == "1":
        swaps += one_counter
    else:
        one_counter += 1

print(swaps)
