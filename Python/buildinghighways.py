# Solution to this problem: https://open.kattis.com/problems/buildinghighways

# Idea: 
# Initially I thought of using Kruskals algorithm for spanning a MST, which surely would hold the correct answer. Allthough a correct solution, I think it was
# too slow for this problem (Time Limit Exceeded). I realized though that the problem can be solved very easily by simple calculating the cost of connecting all
# nodes to nodes of the least cost. Then we can return the sum of every vertix plus (V-1)*least, where least is the cheapest vertix. This formula is derived from
# the simple fact that we connect all V-1 vertices to it. The function calculateLeastCost() does this:

def calculateLeastCost(l):
    least = -1
    s = 0
    for element in l:
        if element < least or least == -1:
            least = element
        s += element
    return s + ((len(l)-1) -1) *least

# 1. Input:
N = int(input())
A = list(map(int,input().split()))
print(calculateLeastCost(A))
