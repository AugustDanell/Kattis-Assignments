def increment_one(x):
    return (x + 1)

end = 365
day = 1

clean_ups = 0
pushes = int(input())
push_list = list(map(int,input().split()))
dirty_list = []
while(day <= end):
    if(day in push_list):
        dirty_list.append(0)

    incremented_list = (list(map(lambda x: increment_one(x), dirty_list.copy())))
    next_day = sum(incremented_list)

    if(next_day >= 20):
       # print(day)
        dirty_list = []
        clean_ups += 1
    else:
        dirty_list = incremented_list.copy()

    day += 1

if(not dirty_list == []):
    print(clean_ups +1)
else:
    print(clean_ups)
