# 706th Kattis, A Solution To The Problem: https://open.kattis.com/problems/flippingpatties

'''
    General Solution: Hashmaps for storing operations
    1. Save every operation to a hashmap.
    2. Iterate over the keys and find the largest.
    3. Remember that a chef can use two hands so every chef in this time step can do 2 operations
    so we will need one chef for every two operations.
'''
orders = int(input())
timeline = {}
for _ in range(orders):
    d,t = list(map(int,input().split()))
    t1 = t-2*d
    t2 = t-1*d
    t3 = t

    if t1 in timeline:
        timeline[t1] += 1
    else:
        timeline[t1] = 1
    if t2 in timeline:
        timeline[t2] += 1
    else:
        timeline[t2] = 1
    if t3 in timeline:
        timeline[t3] += 1
    else:
        timeline[t3] = 1

max_operations = 0
for key in timeline.keys():
    max_operations = max(max_operations, timeline[key])

print((1+max_operations)//2)
