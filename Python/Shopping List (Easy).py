a,b = input().split()
shopping_lists = int(a)
items = int(b)

item_map =  {}
item_list = []
start_list = input().split()

for i in range(shopping_lists -1):
    start_list = [intersect for intersect in input().split() if intersect in start_list]

print(len(start_list))
start_list.sort()
for i in start_list:
    print(i)
