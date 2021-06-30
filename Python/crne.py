import math
cuts = int(input())
pieces = 0

# First we do vertical cuts and we do cuts / 2 of those, ceiled.
verticalCuts = int(math.ceil(cuts/2))+1
cuts = (cuts // 2) + 1

pieces = cuts * verticalCuts
print(pieces)