# Solution to the problem: https://open.kattis.com/problems/smoothiestand

# 1. Take in input and initiate a global profit:
ingredients, recipes = list(map(int,input().split()))
ingredientList = list(map(int,input().split()))
profit = 0

# 2. Iterate over recipes:
for _ in range(recipes):
    data = list(map(int,input().split()))
    sale = data.pop(-1)
    l = []

    # 3. For every recipe append to list l the amount of times an ingredient can be divided, i.e 12/3 -> 4 times:
    for i in range(ingredients):
        if data[i] > ingredientList[i]:
            l.append(0)
            break
        elif data[i] == 0:
          # 4. Also build in a check for division with zero, such ingriedents need not be included anyway:
          continue
        else:
            l.append(ingredientList[i]//data[i])
    
    # 5. Local profit is defined as the min of how many times an ingriedent can be divided times the price:
    local_profit = min(l)*sale

    # 6. If local profit exceeds the old profit, set local profit as the new global max:
    if(local_profit > profit):
        profit = local_profit

# 7. Print the global profit.
print(profit)
