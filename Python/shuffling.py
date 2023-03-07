# Performs an out shuffle:
def outShuffle(l):
    delimiter = 0
    if len(l) % 2 == 0:
        delimiter = len(l) // 2
    else:
        delimiter = len(l)//2 +1

    botHalf = l[:delimiter]
    topHalf = l[delimiter:]
    outList = []
    popBot = True

    while len(botHalf) > 0 or len(topHalf) > 0:
        if popBot:
            outList.append(botHalf.pop(0))
        else:
            outList.append(topHalf.pop(0))

        popBot = not popBot

    return outList

# Performs an in shuffle:
def inShuffle(l):

    delimiter = len(l) // 2
    botHalf = l[:delimiter]
    topHalf = l[delimiter:]
    inList = []
    popTop = True

    while len(botHalf) > 0 or len(topHalf) > 0:
        if popTop:
            inList.append(topHalf.pop(0))
        else:
            inList.append(botHalf.pop(0))

        popTop = not popTop

    return inList

# Check if sequentially ordered:
def checkLinear(l):
    for i in range(1, len(l)):
        if not l[i-1] + 1 == l[i]:
            return False
    return True

# Input:
n, op = input().split()
n = int(n)
l = [i for i in range(n)]
shuffles = 1

# First shuffle + store whatever shuffle we want into a variable:
f = None
if op == "out":
    l = outShuffle(l)
    f = outShuffle
else:
    l = inShuffle(l)
    f = inShuffle

# Shuffle with our stored variable f until we have a sequentially ordered deck:
while not checkLinear(l):
    l = f(l)
    shuffles += 1

# Output required shuffles to get back to the identity permutation.
print(shuffles)
