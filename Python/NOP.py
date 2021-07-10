data_sequence = list(input())

i = 0
NOPS = 0
steps = 3
while i < len(data_sequence):
    letter = data_sequence[i]
    if(letter.isupper()):
        NOPS += 3 - steps
        steps = 0
    else:
        steps += 1
        steps %= 4


    i += 1

print(NOPS)
