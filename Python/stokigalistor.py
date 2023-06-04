# 702th Kattis. A Trivial solution to the problem: https://open.kattis.com/problems/stokigalistor

''' General Solution: Compare to the sorted list.
    A very trivial solution to this problem would be to:
    
    1. Sort the initial list and initiate a counter to 0.
    2. Iterate over the two lists and compare each item.
    3. If they are not the same, increment a counter.
    4. Output the counter.
''' 

N = int(input())
l = list(map(int,input().split()))
sorted_list = sorted(l)
counter = 0
for i in range(N):
    if not l[i] == sorted_list[i]:
        counter += 1
print(counter)
