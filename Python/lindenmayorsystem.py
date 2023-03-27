# A solution to the problem: https://open.kattis.com/problems/lindenmayorsystem

# 1. Initiate maps of rules:
rules, iterations = list(map(int,input().split()))
ruleMapping = {}
for _ in range(rules):
    rule = input().split()
    x,y = rule[0],rule[-1]
    ruleMapping[x] = y

# 2. Read in the starting sequence and initiate it as current:
currentSequence = input()

# 3. For every iteration given create a new sequence as the result of applying the rules of the Lindon Grammar:
for i in range(iterations):
    newSequence = ""
    for c in currentSequence:
        if ruleMapping.__contains__(c):
            newSequence += ruleMapping[c]
        else:
            newSequence += c
    currentSequence = newSequence

# 4. Lastly print the result:
print(currentSequence)
