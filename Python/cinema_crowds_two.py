capacity, groups = list(map(int, input().split()))
group_lists = list(map(int, input().split()))
#group_lists.sort()

fitted = 0
for i in range(groups):
    if(capacity >= group_lists[i]):
        capacity -= group_lists[i]
        fitted += 1
    else:
        break

print(groups - fitted)
