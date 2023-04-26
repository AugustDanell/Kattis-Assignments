# Solution to the problem: https://open.kattis.com/problems/closestsums
import sys

def find_closest(sum_set, query):
    min = -1
    item = -1
    for s in sum_set:
        if min == -1 or abs(query-s) < min:
            min = abs(query-s)
            item = s
    return item

case = 1
for line in sys.stdin:
    print("Case {0}:".format(case))
    case += 1
    n = int(line)
    init_set = []
    for _ in range(n):
        init_set.append(int(input()))

    sum_set = []
    for i in init_set:
        for j in init_set:
            if i == j:
                continue
            else:
                sum_set.append(i+j)

    #print(init_set, sum_set)
    q = int(input())
    for _ in range(q):
        query = int(input())
        print("Closest sum to {0} is {1}.".format(query, find_closest(sum_set, query)))
    #print(n,q)
