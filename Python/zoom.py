# Trick for reading in a list of integer data OR multiple integer arguments with one line of code
n, step_length = list(map(int, input().split()))
dataNumbers = list(map(int, input().split()))

# Fill this list with appropriate numbers:
appendList = []

# Iteration (begin, end, stepsize):
for i in range(step_length -1, n, step_length):
    appendList.append(str(dataNumbers[i]))

# Merge the list into a text line. Use " " instead of "" so that every item is spaced correctly.
print(" ".join(appendList))
