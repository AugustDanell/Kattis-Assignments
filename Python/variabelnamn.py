# 713th Kattis, A Solution To The Problem: 

''' General Solution: Hashmaps for caching
    1. Use a hashmap to store taken variables for constant lookup time.
    2. Use another nestled hashmap for caching.
'''

N = int(input())
taken_marks = {}
cache = {}
for _ in range(N):
    step = int(input())
    v = step
    if v in cache:
        v = cache[v]
    while v in taken_marks:
        v += step

    cache[step] = v
    taken_marks[v] = True
    print(v)
