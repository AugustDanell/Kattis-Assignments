# 672th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/asciifigurerotation

'''
    General Solution:
    1. This solution is a bit messy but what we do is to read in every row into a grid.
    2. We then add padding (whitespaces) according to the longest column.
    3. We then do a rotation where we are replacing - with | and reversing every line in grid.
    4. Lastly we remove the needed padding. If we only have white spaces those lines become [].
    5. We use the join function to print lines that are not [].
'''

first = True
while True:
    rows = int(input())
    if rows == 0:
        break
    elif not first:
        print()

    first = False
    # 1. Construct the initial grid:
    grid = []
    longest_length = rows
    for _ in range(rows):
        row = input()
        grid.append(row)
        longest_length = max(longest_length, len(row))

    # 2. Add Padding for every row:
    for i in range(rows):
        while len(grid[i]) < longest_length:
            grid[i] += " "

    # 3. Do a rotation:
    rotated_grid = []
    for col in range(longest_length):
        append_row = ""
        for row in range(rows):
            new_element = grid[row][col]
            if new_element == "-":
                new_element = "|"
            elif new_element == "|":
                new_element = "-"

            append_row += new_element
        rotated_grid.append(append_row[::-1])

    # 4. Remove padding:
    for i in range(len(rotated_grid)):
        rotated_grid[i] = list(rotated_grid[i])
        only_whitespace = True
        for element in rotated_grid[i]:
            if not element == " ":
                only_whitespace = False
                break

        if only_whitespace:
            rotated_grid[i] = []
            continue

        while rotated_grid[i][-1] == " ":
            rotated_grid[i].pop()

    # 5. Print the rotated grid:
    for line in rotated_grid:
        if not line == []:
            print("".join(line))
