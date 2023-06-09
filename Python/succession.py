# 721th Kattis. A solution to the problem: https://open.kattis.com/problems/succession

''' General Solution: BFS
    1-3: We read in the data and intialize an adjacency list corresponding to a directed
    graph, which is used to model the relationships between parents and children (tree).
    This is then passed to a BFS function.
    
    BFS:
    The BFS will pump the available blood it gets down to its children. As it does this
    the hashmap blood_mapping is iteratively updated. Since hashmaps are mutable objects
    this object will be persistent outside the function. We use deques for faster popleft
    than a normal list (No need for refactoring pertaining to indices). 
    
    4: As a fourth and final step we iterate over every person who is a claimant and we
    have a look at their blood mapping to see who has the greatest claim. We then just
    print that out.
'''

from collections import deque

def BFS(start, adj_list, blood_mapping):
    to_visit = deque([start])
    visited = {}
    while len(to_visit) > 0:
        name,blood = to_visit.popleft()

        if name in adj_list:
            for child in adj_list[name]:
                if child not in blood_mapping:
                    blood_mapping[child] = blood/2
                else:
                    blood_mapping[child] += blood/2
                to_visit.append([child, blood/2])


# 1. Read in data:
N,K = list(map(int,input().split()))
founder = input()
blood_mapping = {founder:1.0}
adj_list = {}

# 2. Init a directed graph pertaining to succession:
for _ in range(N):
    a,b,c = input().split()
    if b in adj_list:
        adj_list[b][a] = True
    else:
        adj_list[b] = {a:True}
    if c in adj_list:
        adj_list[c][a] = True
    else:
        adj_list[c] = {a:True}

# 3. Pass everything to BFS to init bloodmapping
BFS([founder, 1.0], adj_list, blood_mapping)

# 4:
best_person, most_blood = None, 0.0
for _ in range(K):
    person = input()
    blood = 0.0
    if person in blood_mapping:
        blood = blood_mapping[person]

    if blood > most_blood or best_person is None:
        most_blood = blood_mapping[person]
        best_person = person

print(best_person)
