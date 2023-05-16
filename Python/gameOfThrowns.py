# Solution to the problem: https://open.kattis.com/problems/throwns

# Idea:
# Read in the throws one after another and increment it modulo the amount of children in the circle.
# Save the index of where the egg is for every state in a dictionary called "states".
# If an undo operation is read in, extract that state in constant time from "states". 

N,K = list(map(int,input().split()))
egg_index = 0
operations = input().split()
state = 0
states = {0:0}

i = 0
while i < len(operations):
    operation = operations[i]
    if operation == "undo":
        i+= 1
        undo_operations = int(operations[i])
        state = state - undo_operations - 1
        if state in states:
            egg_index = states[state]
        else:
            state = 0
            egg_index = 0
    else:
        egg_index += int(operation)
        egg_index %= N

    states[state] = egg_index
    i+= 1
    state += 1

print(egg_index)
