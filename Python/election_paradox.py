import math

# election paradox
# To garner the maximum of votes yet still losing we should win 100% ceil(half-1) of the largest regions
# In the remaining regions we should lose with 1 vote. To that end we use the very same scheme. 

regions = int(input())
region_list = list(map(int, input().split()))
region_list.sort(reverse=True)
votes = 0

for i in range(math.ceil(regions/2 -1)):
    votes += region_list.pop(0)

for population in region_list:
    votes += math.ceil(population/2 -1)

print(votes)
