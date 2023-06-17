# 730th Kattis: https://open.kattis.com/problems/keepitcool

''' General Solution: Brute Force
    What we can do is to naively insert new cans for as long as we have
    cans / capacity. We insert them on the minimum element. Overall the
    time complexity is O(n**2) but its ok because the problem instance
    is small. We naively insert as many cans as we can on the index where
    there are as few cans as possible. Then we count the cans for the
    indices where there have been no insertions. If this is larger than
    the amount of students(m) then we have a solution, else it is impossible.
'''

# 1. Read in the data:
n,m,s,d = list(map(int,input().split()))
cans = (list(map(int, input().split())))
insertion_list = [0]*s

# 2. Load in the soda cans for as long as we have soda cans or capacity:
while n > 0 and sum(cans) < s*d:
    min_val = min(cans)
    min_index = cans.index(min_val)
    insertion = min(n,d - cans[min_index])
    n -= insertion
    cans[min_index] += insertion
    insertion_list[min_index] = insertion

# 3. Count how many cold soda cans there are:
cold_ones = 0
for i in range(len(cans)):
    if insertion_list[i] == 0:
        cold_ones += cans[i]

# 4. If there are more students than cold cans, output impossible, else output the optimal insertion list:
if m > cold_ones:
    print("impossible")
else:
    print(" ".join(list(map(str,insertion_list))))
