# 709th Kattis, A Solution To The Problem: https://open.kattis.com/problems/hindex

''' General Solution: Hashmaps for subtraction
    1. Add a hashmap for subtraction, for example, if we are at H = 2, we cannot use
    the index 1, so we can subtract them from the total.
    
    2. Do this until it holds true that the remaining total is less than the H_index.
'''

N = int(input())
h_map = {}
for _ in range(N):
    index = int(input())
    if index in h_map:
        h_map[index] += 1
    else:
        h_map[index] = 1

h_index = 0
while True:
    if h_index in h_map:
        N -= h_map[h_index]

    if N <= h_index:
        break
    h_index += 1
print(h_index)
