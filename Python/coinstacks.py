# 729th Kattis, A Solution to the problem: https://open.kattis.com/problems/coinstacks

''' General Solution: Brute Force
    A Brute force solution where the first player takes from the highest stack and the
    other player takes from the second highest stack, provided that the conditions for
    a valid solution is met. 
'''

# 1. Read in the data:
N = int(input())
stacks = list(map(int,input().split()))
largest_stack = max(stacks)
stack_sum = sum(stacks)

# 2. See that the conditions for a solution is met:
if largest_stack*2 > stack_sum or stack_sum%2 == 1:
    print("no")
    
# 3. If they are, brute force a solution in O(n**2) time. 
else:
    print("yes")
    for i in range(stack_sum//2):
        highest_index = 0
        highest_val = stacks[0]
        for i in range(len(stacks)):
            if stacks[i] > highest_val:
                highest_val = stacks[i]
                highest_index = i
        stacks[highest_index] -= 1

        highest_index_two = (highest_index+1)%len(stacks)
        highest_val_two = stacks[highest_index_two]
        for i in range(len(stacks)):
            if i == highest_index:
                continue

            if stacks[i] > highest_val_two:
                highest_val_two = stacks[i]
                highest_index_two = i
        stacks[highest_index_two] -= 1

        print(highest_index+1, highest_index_two+1)
