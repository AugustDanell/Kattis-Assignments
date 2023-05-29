#696th Kattis, Trivial Solution to the problem: https://open.kattis.com/problems/risdomare

''' General Solution: Find the global max and then max based on category.
    1. First we just iterate over l and find the largest max sum as we append (a,b) to l.
    2. We iterate over l and based on a preference we find the largest a or b where the
       condition holds that (a+b) = MAX. Straight forward. 
'''

N = int(input())
antal = "antal" == input().strip()

# 1. Find the max sum:
l = []
max_sum = 0
for _ in range(N):
    a,b = list(map(int,input().split()))
    l.append([a,b])
    if a+b > max_sum:
        max_sum = a+b

# 2. Given a sorting preference, find the max within that category:
max_index = 0
max_agg = 0
for index in range(N):
    if(sum(l[index]) == max_sum):
        if (antal) and l[index][0] > max_agg:
            max_index = index+1
            max_agg = l[index][0]
        elif not antal and l[index][1] > max_agg:
            max_index = index +1
            max_agg = l[index][1]

# 3. Print the index for the max:
print(max_index)
