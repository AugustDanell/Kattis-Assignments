# A somewhat hairy solution to the problem: https://open.kattis.com/problems/ghostleg

# A function that for every element prints its 1-indexed position.
def inverse(l):
    for i in range(1, len(l)+1):
        index = l.index(i)
        print(index+1)

# 1. Input, initiate an adjacency matrix for transfer between different legs:
N,M = list(map(int,input().split()))
adj_matrix = {}
for i in range(N):
    adj_matrix[i+1] = {}

# 2. Read in the horizontal transitions and use a depth counter that is read in as a value:
depth = 0
for _ in range(M):
    depth += 1
    n = int(input())
    a, b = n, n+1
    if not adj_matrix[a].__contains__(b):
        adj_matrix[a][b] = [depth]
    else:
        adj_matrix[a][b].append(depth)

    if not adj_matrix[b].__contains__(a):
        adj_matrix[b][a] = [depth]
    else:
        adj_matrix[b][a].append(depth)

# 3. Iterate over every node n:
l = []
for n in range(1, N+1):
    depth = 0

    # 4. For as long as we can we make transitions and update our current depth:
    while(adj_matrix.__contains__(n)):
        new_node = -1
        best_depth = -1
        for key in adj_matrix[n]:
            transitions = adj_matrix[n][key]
            for transition in transitions:
                if transition > depth:
                    if best_depth == -1 or transition < best_depth:
                        best_depth = transition
                        new_node = key
        
        # 5. If we find a transition we transition to the highest possible. If no eligble transitions are available we append our current position and break:
        if new_node == -1:
            l.append(n)
            break
        else:
            n = new_node
            depth = best_depth

# 6. Now our answer will be the current index of every node, so we put that into a function which prints that for us
inverse(l)
