'''
    Solution idea:
    Read in the data and do the following steps:

    1. Insert the initial people in the queue.
    2. Handle operations within the queue, they can be:
    a: Person leaving, in which case just remove them from the queue, or
    b: Someone cutting the line, in which case increment up to that specific index and insert them there.
    3: Just print every element.
'''

people = int(input())
queue = []

# 1: Inserting people into the queue.
for i in range(people):
    queue.append(input())

# 2: Handle operations
operations = int(input())
for i in range(operations):
    inp = input().split()
    operation = inp[0]


    if(operation == "cut"):
        index = 0
        a = inp[1]
        b = inp[2]
        while(not b == queue[index]):
            index += 1

        queue.insert(index, a)

    elif(operation == "leave"):
        a = inp[1]
        queue.remove(a)

# 3: Print the queue:
for e in queue:
    print(e)
