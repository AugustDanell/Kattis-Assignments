n = int(input())
total = 0
pizzas = []
for _ in range(n):
    name,cost = input().split()
    cost = int(cost)
    pizzas.append(cost)

sortedPizzas = sorted(pizzas, reverse=True)
for i in range(0,n,2):
    total += sortedPizzas[i]
print(total)