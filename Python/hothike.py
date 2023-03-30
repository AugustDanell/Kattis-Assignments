# Solution to the problem: https://open.kattis.com/problems/hothike

# 1. Initiate global counters:
d = int(input())
days = list(map(int,input().split()))
global_min = 0
global_index = 0

# 2. Iterate over each day
for i in range(1, d-1):
    prev_day = days[i-1]
    next_day = days[i+1]
    local_max = max(prev_day, next_day)
    
    # 3. If the previous day or the next day are cool, store them as a global min:
    if i == 1 or local_max < global_min:
        global_min = local_max
        global_index = i

# 4. Print the result:
print("{0} {1}".format(global_index, global_max))
