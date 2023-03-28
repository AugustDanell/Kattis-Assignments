# Solution to the problem: https://open.kattis.com/problems/hermits

# 1. Initiate two lists, one with the business and later one with the sum of crossings:
n = int(input())
a_i = list(map(int,input().split()))
s_i = []
for i in range(n):
    s_i.append(a_i[i])

# 2. Increment the sums of different indices pertaining to crossing of other streets:
m = int(input())
for _ in range(m):
    v1,v2 = list(map(int,input().split()))
    s_i[v1-1] += a_i[v2-1]
    s_i[v2-1] += a_i[v1-1]

# 3. Simply find the lowest sum and if there are multiple such, the lowest index:
lowest = 0
index = 0
for i in range(n):
    if i == 0 or s_i[i] < lowest:
        lowest = s_i[i]
        index = i

# 4. Print that index. Increment with one to adjust for one-indexed problem:
print(index+1)
