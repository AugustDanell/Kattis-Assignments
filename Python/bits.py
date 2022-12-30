n = int(input())
for i in range(n):
    numberString = input()
    maxBits = 0

    for j in range(1, len(numberString)+1):
        substring = numberString[0:j]
        bitstring = bin(int(substring))
        bits = 0
        for bit in bitstring:
            if(bit == "1"):
                bits += 1

        if bits > maxBits:
            maxBits = bits
    print(maxBits)
