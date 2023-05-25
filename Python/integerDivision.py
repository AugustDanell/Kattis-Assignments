# My 687th Kattis. A solution to the problem: https://open.kattis.com/problems/integerdivision

''' General Solution:
    To visualize every solution that is to say, every way to pair divisors, we can think of a complete graph.
    We sum over the pairs that every element form over a remainder. For example if 3 elements all have a remainder of 1 after
    division then for this example we sum a complete 3-graph, adding 3 to the total. We then just print the total.
'''

def edges_in_complete_graph(n):
    return n*(n-1)//2

N,D = list(map(int,input().split()))
l = list(map(int,input().split()))
vals = {}
for element in l:
    division = element // D
    if division in vals:
        vals[division] += 1
    else:
        vals[division] = 1

total = 0
for key in vals.keys():
    total += edges_in_complete_graph(vals[key])

print(total)
