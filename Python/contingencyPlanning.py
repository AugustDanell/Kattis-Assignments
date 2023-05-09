def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n-1)*n
def fac_ones(bin_str):
    counter = 0
    for c in bin_str:
        if c == "1":
            counter += 1
    return fac(counter)

N = int(input())
sequences = 0
too_many = False
for i in range(1, 2**(N)):
    bin_str = bin(i)[2:]
    sequences += fac_ones(bin_str)
    if sequences > 1e9:
        too_many = True
        break

if too_many:
    print("JUST RUN!!")
else:
    print(sequences)
