# 717th Kattis, A Solution To The Problem: https://open.kattis.com/problems/dingdongditch

''' General Solution: Hashmap for constant lookup.
    1. For this problem we can just iterate over each house level and save it in a hashmap.
    2. We can then access it in constant time.
'''

# 1. Create a minimum mapping for every level:
N,Q = list(map(int,input().split()))
sorted_houses = sorted(list(map(int,input().split())))
house_mapping = {}
acc = 0
for i in range(N):
    acc += sorted_houses[i]
    house_mapping[i+1] = acc

# 2. Print the level for each person:
people = list(map(int,input().split()))
for person in people:
    print(house_mapping[person])
