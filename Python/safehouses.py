# A solution to the problem: https://open.kattis.com/problems/safehouses

# Calculate manhattan distance:
def manhattan(spy,house):
    x1,y1 = spy
    x2,y2 = house
    return abs(x1-x2) + abs(y1-y2)

# 1. Read in the coordinates of spies and safe houses:
rows = int(input())
spy_list = []
safe_list = []
for y in range(rows):
    row = list(input())
    while row.__contains__("S"):
        index = row.index("S")
        spy_list.append([index, y])
        row[index] = "."
    while row.__contains__("H"):
        index = row.index("H")
        safe_list.append([index,y])
        row[index] = "."

# 2. Iterate over every spy and every safe house:
global_max = -1
for spy in spy_list:
    closest = 0

    # 3. For every spy, calculate the nearest safe house:
    for h_i in range(len(safe_list)):
        house = safe_list[h_i]
        dist = manhattan(spy,house)
        if h_i == 0 or dist < closest:
            closest = dist
    
    # 4. Save to global max if spy_i has a longer route to any safe house than what is currently stored:
    if closest > global_max:
        global_max = closest

# 5. Print the global max:
print(global_max)
