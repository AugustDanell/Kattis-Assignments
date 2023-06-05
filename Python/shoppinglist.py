# 708th Kattis, A Solution To the problem: https://open.kattis.com/problems/shoppinglist
''' General Solution: Just iterate over each line and use hashmaps to keep count.
'''

N,P = list(map(int,input().split()))
product_map = {}
final_list = []
for _ in range(N):
    products = input().split()
    handled_product = {}
    for product in products:
        if product in handled_product:
            continue
        else:
            handled_product[product] = True

        if product in product_map:
            product_map[product] += 1
        else:
            product_map[product] = 1

        if product in product_map and product_map[product] == N:
            final_list.append(product)

print(len(final_list))
sorted_list = list(sorted(final_list))

for product in sorted_list:
    print(product)
