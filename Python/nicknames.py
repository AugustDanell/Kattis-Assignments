# 716th Kattis, A Solution To The Problem: https://open.kattis.com/problems/nicknames

''' General Solution: Nestled hashmaps for prefix problem.
    In this problem we are dealing with prefix matching. I did a similar problem with phone numbers yesterday
    One way to solve this problem in acceptable time is to use hashmaps. 
    1. We can nestle each character in a hashmap. This time we match every sub_str with a number.
    2. When we then iterate over each nickname we can in constant time extract how many names map to it.

'''

# 1. Map the substr of every real name:
N = int(input())
names = {}
for _ in range(N):
    name = input()
    for i in range(len(name)):
        sub_str = name[:i+1]

        if sub_str in names:
            names[sub_str] += 1
        else:
            names[sub_str] = 1

# 2. Read in the nicknames and match them to the map:
Q = int(input())
for _ in range(Q):
    nickname = input()
    if nickname in names:
        print(names[nickname])
    else:
        print(0)
