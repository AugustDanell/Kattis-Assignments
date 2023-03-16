# A general function for lambda expression:
def sortOnMapping(x,d):
    return d[x]

# Input:
N,K = list(map(int,input().split()))
mapping = {}
colorList = []
for i in range(1, (K+1)):
    mapping[i] = 0
    colorList.append(i)

# Mapping:
colors = list(map(int,input().split()))
for color in colors:
    mapping[color] += 1

# Sort with a lambda function as a key:
f = lambda x: sortOnMapping(x, mapping)
sortedColors = sorted(colorList, key = f)

# Code to filter out bad answers:
filteredColors = []
prev = mapping[sortedColors[0]]
while len(sortedColors) > 0 and prev == mapping[sortedColors[0]]:
    prev = mapping[sortedColors[0]]
    filteredColors.append(sortedColors.pop(0))

# Sort the list of filtered colors and use map to convert every member of the list into a str so we can join it:
sortedFilteredColors = list(map(str, sorted(filteredColors)))
print(len(sortedFilteredColors))

# Print the answer:
print(" ".join(sortedFilteredColors))
