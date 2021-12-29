blocks = int(input())
level = 0
used_blocks = 0
squared_cost = 1

while (used_blocks < blocks):
    used_blocks += squared_cost**2
    if used_blocks > blocks:
        break

    level += 1
    squared_cost += 2

print(level)
