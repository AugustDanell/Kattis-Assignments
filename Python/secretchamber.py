# Solution to the problem: https://open.kattis.com/problems/secretchamber

# A naive BFS. We return true if we can find the target and false otherwise, provided that we have the adj_matrix of a directed graph:
def bfs(start, target, adj_matrix):
    to_visit = [start]
    visited = {}
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if current == target:
            return True
        else:
            if visited.__contains__(current):
                continue
            else:
                if adj_matrix.__contains__(current):
                    for next_node in adj_matrix[current]:
                        to_visit.append(next_node)
        visited[current] = True

    return False
# 1. Read in data, read in the symbol mapping into an adjacency list:
symbols, words = list(map(int,input().split()))
adj_matrix = {}

# 2. Initiate an adjacency matrix for a directed graph. If it was undirected we could append b -> a for every row:
for _ in range(symbols):
    a,b = input().split()

    if not adj_matrix.__contains__(a):
        adj_matrix[a] = [b]
    else:
        adj_matrix[a].append(b)

# 3. For every word, pass its letters into a BFS search, attempting to transform the current letter to the target:
for _ in range(words):
    word, word2 = input().split()
    
    # 4. If their lengths do not match we can already say that a tranformation is impossible:
    if not len(word) == len(word2):
        print("no")
    else:
        # 5. For every word we attempt the BFS. If no BFS path is found we exit prematurely and flag the boolean no_solution:
        no_solution = False
        for i in range(len(word)):
            start  = word[i]
            target = word2[i]
            if not bfs(start, target, adj_matrix):
                print("no")
                no_solution = True
                break
        
        # 6. By now, if no_solution is still false, we know that every letter could be transformed and our target word reached:
        if not no_solution:
            print("yes")
