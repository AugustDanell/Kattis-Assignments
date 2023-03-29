# A simple solution to the problem: https://open.kattis.com/problems/froshweek2

# 1. Take in two lists of descendingly sorted tasks and intervals:
n,m = list(map(int,input().split()))
rev_sorted_tasks = sorted(list(map(int,input().split())), reverse= True)
intervals = sorted(list(map(int,input().split())), reverse = True)

# 2. Iterate over every task. If all intervals are taken, just exit:
count = 0
for task in rev_sorted_tasks:
    if len(intervals) == 0:
        break
    
    # 3. Else, see if we can match the longest interval with the longest task. If we can increment counter and pop the interval:
    index = 0
    if intervals[0] >= task:
        count += 1
        intervals.pop(0)

# 4. Lastly, print out the counter:
print(count)
