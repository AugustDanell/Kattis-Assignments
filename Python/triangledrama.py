# A solution to the problem: https://open.kattis.com/problems/triangledrama

# Define a function to sort a triangle with weighed values, later this function is passed as the key arg at the end:
def sortTrio(trio):
    return trio[0]*100 + trio[1]*10 + trio[2]

# 1. Input, initiate a matrix and create a max attraction global counter and its corrosponding list for best trios:
people = int(input())
matrix = []
for _ in range(people):
    matrix.append(list(map(int,input().split())))
max_attraction = 0
bestTrios = []

# 2. Iterate over each row in the matrix:
for r in range(len(matrix)):
    row = matrix[r]
    
    # 3. For each row, iterate over each two pairs of indices, i and j, where i ==//== j:
    for i in range(len(row)):
        for j in range(len(row)):
            if i == j:
                continue
            
            # 4. Calculate the attraction value of the triangle:
            attraction = row[i]*row[j]*matrix[i][j]

            # 5. If it is a new max, flush the previous best trio and create a new one and set the counter. If it is the same as the max, append the new value:
            if attraction > max_attraction:
                max_attraction = attraction
                bestTrios = [[r+1, i+1, j+1]]
            elif attraction == max_attraction:
                bestTrios.append([r+1, i+1, j+1])

# 6. Best trios now holds the best trios as tripplets, but we also want to sort them properly. Do this by taking the first element in the sorted version with our function as a key:
bestTrio = (sorted(bestTrios, key=sortTrio))[0]

# 7. Now best trio holds three integers (a,b,c) as its answer. We simply convert them all to a string and apply the join function and output the answer:
print(" ".join(list(map(str,bestTrio))))
