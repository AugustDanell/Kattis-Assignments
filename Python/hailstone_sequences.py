current = int(input())
length = 1
while not current == 1:
    if(current % 2 == 0):
        current = current // 2
    else:
        current = current*3 + 1

    length += 1

print(length)
