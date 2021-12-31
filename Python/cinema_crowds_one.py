'''
    Very similar to cinema crowds two but instead of closing down the theatre
    when there is a missfit, the group itself goes. So for instance if the capacity
    is C = 10, and we have, 1, 2, 3, 6, 1, 1, 1, the teatre will let in 6 groups
    whereas in version two of the problem it will close down at the 6-man group
    and so only let in 3. That is the difference between the two. 
'''


capacity, groups = list(map(int, input().split()))
group_lists = list(map(int, input().split()))
#group_lists.sort()

fitted = 0
for i in range(groups):
    if(capacity >= group_lists[i]):
        capacity -= group_lists[i]
        fitted += 1
    else:
        pass
        #break

print(groups - fitted)
