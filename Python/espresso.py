'''
    1. First we read in the data using the format below to easily do it.
    2. We take in every order and reduce our current capacity.
    3. If the capacity is less than what is required we fill up our can,
       incrementing the amount of refills by one.
    4. We simply output the refills. 
'''


orders, fill = list(map(int,input().split()))
current_capacity = fill
refills_done = 0

for i in range(orders):
    data = list(input())
    cost = int(data[0])

    if(len(data) == 2):
        cost += 1

    if(current_capacity < cost):
        refills_done += 1
        current_capacity = fill

    current_capacity -= cost

print(refills_done)
