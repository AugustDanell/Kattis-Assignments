min = int(input())
breaks = 0
squares = 1
okPieces = []  # A list for pieces < min, if we take (min - pieces) > 0, we need not consider them.
okPieceSum = 0 # Remove ok pieces from the count

while(squares < min):
    squares = squares * 2

origSquares = squares
while(min > 0):
    if(squares <= min):
        min = min - squares
    else:
        squares = int (squares/2)
        breaks = breaks + 1

print(origSquares, breaks)