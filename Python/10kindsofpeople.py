# Solution to the problem: https://open.kattis.com/submissions/10892668

# General Solution idea:
'''
At first when I attempted this problem I got time limit exceeded when I made a brute force attempt of using a BFS trying to go from (r1,c1) -> (r2,c2).
A better solution can be to create "countries". Essentially we can start at every node in the grid and then use a BFS. Every node that is visited will be
transformed to a label for a country. Decimal countries will have a value > 0 and binary countries < 0. We can use this algorithm to transform one to the other.
For example: [1,1,0,0] -> [2,2,-3,-3].
When we then get a query asking for (r1,c1) -> (r2,c2), we can in constant lookup time check if they belong to the same country and output accordingly
'''

# get_hash_value: This function is used to produce a unique hashvalue pertaining to a row and a col value, given that both cannot be over 1000:
def get_hash_value(x,y):
    return x*10000 + y

def DFS_create_countries(grid, rows, cols, start_row, start_col, country):
    # 1. Initiate a comp value. Either this will be 1 or 0. This is used to see all the squares that are connected to create a "country":
    comp_value = grid[start_row-1][start_col-1]
    to_visit = [[start_row, start_col]]
    visited = {get_hash_value(start_row, start_col) : True}

    # 2. We iterate over it in a DFS fashion:
    while len(to_visit) > 0:

        # 3. Pop a current row and col and brand the corrosponding cell in the grid according to the country label. Differentiate between decimal and binary:
        r,c = to_visit.pop()
        if comp_value == 1:
            grid[r-1][c-1] = country
        else:
            grid[r - 1][c - 1] = -country
        
        # 4. Find a set of new nodes in all the cardinal directions:
        new_nodes = [[r,c-1], [r, c+1], [r-1, c], [r+1, c]]

        # 5. Iterate over each such node individually:
        for new_node in new_nodes:
            r_new, c_new = new_node

            # 6. For each such node, disqualify it if it is out of bounds, already visited (using our hash value) or if it is of another currency than comp:
            if (r_new < 1) or (r_new > rows) or (c_new < 1) or (c_new > cols):
                continue
            elif get_hash_value(r_new, c_new) in visited:
                continue
            elif not grid[r_new-1][c_new-1] == comp_value:
                continue
            
            # 7. If the new node passes all these checks, mark it as visited and append it for new traversals:
            visited[get_hash_value(r_new,c_new)] = True
            to_visit.append([r_new, c_new])

if __name__ == "__main__":

    # 1. Initiate the grid:
    rows,cols = list(map(int,input().split()))
    grid = []
    for _ in range(rows):
        grid.append(list(map(int,list(input()))))
    
    # 2. Iterate over each node/cell and start a BFS there if it does not have a country yet:  
    country_label = 2
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            if grid[row-1][col-1] in [0, 1]:
                DFS_create_countries(grid, rows, cols, row, col, country_label)
                country_label += 1

    # 3. Handle queries. This is done in constant time. If the two queried coordinates are in the same country we can immediately output the answer:
    queries = int(input())
    for _ in range(queries):
        r1,c1,r2,c2 = list(map(int,input().split()))
        if not grid[r1-1][c1-1] == grid[r2-1][c2-1]:
            print("neither")
        elif grid[r1-1][c1-1] > 0:
            print("decimal")
        else:
            print("binary")

    #print(grid)
