'''
    Algoritmic idea:
    1. We read in the data and declare an offset for how much tilted to the left our cursor is.
    2. We then iterate through each character c in the line of text. When a 'L' is accounted we
    increment the offset and decrement it with R. If a B comes we remove the element to the left
    of the cursor. Else we just append the character.
    3. Lastly we output the message.
'''

# 1. Data input and fields:
line = input()
left_tilted = 0
reconstructed = []

# 2. Iterating through each character with respect to L,B and R:
for c in line:
    length = len(reconstructed)
    if c == 'L' and left_tilted < length:
        left_tilted += 1
    elif c == 'R' and left_tilted > 0:
        left_tilted -= 1
    elif c == 'B' and not length == left_tilted:
        reconstructed.pop(length-left_tilted-1)
    else:
        reconstructed.insert(length - left_tilted, c)

    #print('TEST, char: ', c, 'left tilt:', left_tilted)

# 3. Output
print(''.join(reconstructed))
