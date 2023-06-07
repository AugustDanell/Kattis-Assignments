# 714th Kattis Solution: A Solution To The Problem: https://open.kattis.com/problems/basicprogramming2

''' General Solution: Handle every case, use hashmaps for constant lookup time.
    Most challenging time complexically would be case t = 1. 
    In this case we should see if two items in the list, x, y, can be found, where x + y = 7777.
    I solved this case by adding every item as a "needed bit" before, in this way we can iterate
    over every x in linear time and for each iteration we can see if there is a needed bit (7777-x).
    This way we can simply check the first case (t = 1) in linear time. 
'''

N, t = list(map(int, input().split()))
bits = list(map(int, input().split()))
check_map = {}
needed_bits = {}
if(t == 1):
    found = False
    for bit in bits:
        needed_bits[bit] = True
    for bit in bits:
        if (7777 - bit) in needed_bits:
            found = True
            break
    print(["No", "Yes"][found])

elif (t == 2):
    checkMap = {}
    unique = True
    for bit in bits:
        if checkMap.__contains__(bit):
            print("Contains duplicate")
            unique = False
            break

        checkMap[bit] = True

    if unique:
        print("Unique")

elif (t == 3):
    count = {}
    found = False
    for bit in bits:
        if not count.__contains__(bit):
            count[bit] = 1
        else:
            count[bit] += 1

        if count[bit] > N / 2:
            print(bit)
            found = True
            break

    if not found:
        print(-1)

# Probably ok:
elif (t == 4):
    sortedAns = sorted(bits)
    midpoint = len(sortedAns) // 2
    if len(sortedAns) % 2 == 0:
        print(sortedAns[midpoint - 1], sortedAns[midpoint])
    else:
        print(sortedAns[midpoint])

elif (t == 5):
    sortedAns = sorted(bits)
    eligbleBits = []
    for bit in sortedAns:
        if bit >= 100 and bit <= 999:
            eligbleBits.append(str(bit))
        elif bit > 999:
            break
    if not eligbleBits == []:
        print(" ".join(eligbleBits))
