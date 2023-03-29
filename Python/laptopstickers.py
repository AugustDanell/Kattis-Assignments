# A solution to the problem: https://open.kattis.com/problems/laptopstickers

# 1. Input: Initiate an empty grid and read in dimensions:
cols, rows, stickers = list(map(int,input().split()))
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append("_")
    grid.append(row)

# 2. Iterate over each sticker, starting with "a". For each sticker, provided that they are within bounds, put them on:
sticker = "a"
for _ in range(stickers):
    l,h,x_offset,y_offset = list(map(int,input().split()))
    
    # 3. A out of bounds check. If we are within bounds, set grid[Y][X] = sticker. This will override previous stickers: 
    for x in range(l):
        for y in range(h):
            X,Y = x+x_offset, y+y_offset
            if(X < cols and Y < rows):
                grid[Y][X] = sticker
    
    # 4. Using chr and ord what we do is we turn sticker "a" into sticker "b", since it is next in the ascii table.. b -> c -> d ... -> z:
    sticker = chr(ord(sticker)+1)

# 5. When we have plastered every sticker we simply print every row.
for row in grid:
    print("".join(row))
