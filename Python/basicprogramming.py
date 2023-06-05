# 705th Kattis, A Solution To The Problem: https://open.kattis.com/problems/basicprogramming1

''' General Solution: Precalculations + Queries
    We start with doing som precalculations which is to say we calculate the even sum, module
    and the total sum as precalculations. For every query we can then in constant time output it
    was the intital idea (though there is only 1 query, I missed that initially). All the queries
    are in O(N). Many of them are more tightly bound. 
'''

N, t = list(map(int,input().split()))
A    = list(map(int,input().split()))

array_sum = 0
even_sum = 0
modulurized = []
for element in A:
    if element % 2 == 0:
        even_sum += element
    array_sum += element
    modulurized.append(str(chr(97+element%26)))


if t == 1:
    print(7)

elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")

elif t == 3:
    l = sorted([A[0], A[1], A[2]])
    print(l[1])

elif t == 4:
    print(array_sum)

elif t == 5:
    print(even_sum)

elif t == 6:
    print("".join(modulurized))

elif t == 7:
    next_visit = 0
    visited = {}
    while True:
        visited[next_visit] = True
        next_visit = A[next_visit]
        if next_visit >= len(A):
            print("Out")
            break
        elif next_visit == N-1:
            print("Done")
            break
        elif next_visit in visited:
            print("Cyclic")
            break
