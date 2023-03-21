# A solution to the problem: https://open.kattis.com/problems/iwannabe

# A function used to create lambda functions for sorting on a specific category:
def sortOnIndex(l, i):
    return l[i]

# A function that exhaustively empties the list top down based on the problem description:
def checkList(f, d, l):
    counter = 0
    l = list(sorted(l, key = f, reverse=True))
    for i in range(K):
        pokemon = l[i][0]
        if not d.__contains__(pokemon):
            d[pokemon] = True
            counter += 1
    return counter

# 1. Input:
N,K = list(map(int,input().split()))
l = []

# 2. Put the stats into a list, where there is a ID used as a key on the first index:
for i in range(N):
    attack,defense,health = list(map(int,input().split()))
    pokemon = [i, attack, defense, health]
    l.append(pokemon)

# 3. Create 3 lambda functions to be passed in as keys for sorting and a dictionary that is used to store already taken pokemons (since dictionary is mutable):
f1  = lambda l : sortOnIndex(l, 1)
f2 = lambda l : sortOnIndex(l, 2)
f3  = lambda l : sortOnIndex(l, 3)
picked = {}

# 4. Calculate the total as the sum of exhausting the list based on every category:
total = checkList(f1, picked, l) + checkList(f2, picked, l) + checkList(f3, picked, l)

# 5. Print out the calculated total: 
print(total)
