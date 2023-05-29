# 693th Kattis. A solution to the problem: https://open.kattis.com/problems/colourwars

''' General Solution: Complete Graph
    We can model the problem as a graph. Every time a new amount of ppl comes we add it
    to the mapping. For example if a person says that 3 ppl voted like them we add a 
    graph structure of 4 nodes where we count this person as being one of them and add
    the total. If another person with 4 comes in we decrement it to 2, and then if another
    person comes we aggain decrement it to 1. If we reach 0 we have to create a new 4-V
    graph. Then we just print the total.
'''

queries = int(input())
mapping = {}
people = list(map(int,input().split()))
total = 0
for person in people:
    if person not in mapping or mapping[person] == 0:
        total += person +1
        mapping[person] = person
    else:
        mapping[person] -= 1

print(total)
