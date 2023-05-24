# 686th Kattis Solution. Solution to the problem: https://open.kattis.com/problems/starbattles1

''' General Solution:
    Set a flag called valid and assume it to be true, then undergo the process of trying to falsify it:
    1. Count each star for every row that is inputted.
    2. For each such row also keep track of each column for that specific star, save this in a hashmap.
    3. Also check each star with a region, this too is saved in a hashmap.
    4. Iterate over each column and over each region and check so that every one of them has 2 stars.
    5. Lastly, check that every star does not neighbour another star.
''' 

regions = []
for _ in range(10):
    regions.append(list(map(int,list(input()))))

region_mapping = {}

grid = []
cols = {}
valid = True
for r in range(10):
    row = list(input())
    stars = 0
    for c in range(len(row)):
        if row[c] == ".":
            continue

        if c in cols:
            cols[c] += 1
        else:
            cols[c] = 1
        stars += 1

        region = regions[r][c]
        if region in region_mapping:
            region_mapping[region] += 1
        else:
            region_mapping[region] = 1

    grid.append(row)
    if not stars == 2:
        valid = False


for col in range(10):
    if col not in cols or not cols[col] == 2:
        valid = False

for region in range(10):
    if region not in region_mapping or not region_mapping[region] == 2:
        valid = False

for r in range(10):
    for c in range(10):
        if grid[r][c] == ".":
            continue

        r_goto = [r-1, r, r+1]
        c_goto = [c-1, c, c+1]
        for r_next in r_goto:
            for c_next in c_goto:
                if (r_next == r and c_next == c) or r_next < 0 or r_next > 9 or c_next <0 or c_next > 9:
                    continue
                if grid[r_next][c_next] == "*":
                    valid = False

print(["invalid", "valid"][int(valid)])
