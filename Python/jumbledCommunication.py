def scramble(x):
    # Values up to 255 = 11111111 -> 8 bits
    y = 0
    bitNumber = 1
    eightMask = 255 # 255 = 111111111
    for i in range(256):
        z = y
        z = (z ^ (z << 1)) & eightMask

        if(z == x):
            break
        y = y+1

    return str(y)

n = int(input())
data = input()
split = data.split()

ans = ""
for i in range(n):
    ans = ans + " " + scramble(int(split[i]))

print(ans[1:])