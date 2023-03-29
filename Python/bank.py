# Solution to the problem: https://open.kattis.com/problems/bank

# A function used to define the sorting order:
def sort_order(element):
    return -element[1]*100000 + element[0]

# A function tailored to counting the aggregated amount of money in a list of served ppl:
def count(l):
    s = 0
    for person in l:
        s += person[0]
    return s

# Find the person with the least deposited money in the list l and his index:
def min_person(l):
    m = 0
    index = 0
    for i in range(len(l)):
        person = l[i]
        if i == 0 or person[0] < m:
            m = person[0]
            index = i
    return m, index

# 1. Take in input and initate a list:
N,T = list(map(int,input().split()))
l = []

# 2. Append people to that list, where a person is an item of [money, time]:
for _ in range(N):
    l.append(list(map(int,input().split())))

# 3. Apply the custom made sorting function to sort based on time first and then money, if time step is the same:
sorted_l = sorted(l, key=sort_order, reverse= True)

# 4. Initiate a total time and a list for served people. If we have time we just push people to the list for served time. 
total_time = 0
served_people = []
for person in sorted_l:
    if total_time <= person[1]:
        served_people.append(person)
        total_time += 1
    else:
        # 5. If we are out of time on a specific person with a time step, we look to see if a swap is worth it:
        min_p, index = min_person(served_people)
        if person[0] > min_p:
            served_people[index] = person

# 6. We use a function to count the money for every served person and output that:
print(count(served_people))
