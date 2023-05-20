# My 675th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/skolvagen?tab=metadata

'''
    General Solution:
    1. Remove all the both ways in the assignment. Wherever they are we dont care we have to cross once anyways.
    2. Iterate over the roads and if our next road is a south road pass it to sequence_south, else to sequence_north.
    a) Sequence_south: Replace every sequence of |S| > 2, with one and change direction for north = south. 
    Special case if |l| == 1, then we go north.
    b) Sequence_north: Basically the same in reverse but for the special case |l| = 1 we still go north.
'''

from collections import deque

def sequence_north(l, north):
    if not north:
        l.popleft()
        return 0, False

    elif len(l) > 1 and l[0] == "N" and l[1] == "N":
        while len(l) > 0 and l[0] == "N":
            l.popleft()
        return 1, False

    elif len(l) == 1:
        l.popleft()
        return 1, True

    else:
        l.popleft()
        return 1, True

def sequence_south(l, north):
    if north:
        l.popleft()
        return 0, True
    elif len(l) > 1 and l[0] == "S" and l[1] == "S":
        while len(l) > 0 and l[0] == "S":
            l.popleft()
        return 1, True
    elif len(l) == 1:
        l.popleft()
        return 1, True
    else:
        l.popleft()
        return 1, False

line = input()
both = line.count("B")
line = line.replace("B", "")
line = deque(list(line))
crossings = 0
north = True

while len(line) > 0:
    if line[0] == "S":
        local_crossings, north = sequence_south(line, north)
    else:
        local_crossings, north = sequence_north(line, north)
    crossings += local_crossings

print(crossings + both + int(not north))

