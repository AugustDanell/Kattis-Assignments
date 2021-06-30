# Solution to "Hard Drive"
data = input().split()
n = int(data[0]) # Total bits.
c = int(data[1]) # Bit changes.
b = int(data[2]) # Broken bits.

brokenList = []
brokenBits = input().split()
for i in range(b):
    brokenList.append(int(brokenBits[i]))

prev = -1
s = []
#print(brokenList)

nextBroken = brokenList[0]
ind = 0

for i in range(1, n+1):

    if(c == 0):
        # Fill it with ones:
        if(prev == 1):
            #s.append("1")
            d = n - i
            s.append("1"*(d+1))
            prev = 1
            break

        # Fill with zeros:
        else:
            d = n - i
            s.append("0" * (d+1))
            prev = 0
            break

    if(i == nextBroken):
        if(ind < b-1):
            ind += 1
        nextBroken = brokenList[ind]

        # Fill with zeros:
        if(prev == 1):
            c -= 1

        s.append("0")
        prev = 0
        continue

    if(c == 1):
        # Special case, c = 1:
        # This is the end case, with two routes, prev = 1 || prev = 0

        if(prev == 1):
            # Assuming prev is 1, we need just append a zero (guaranteed).
            c -= 1
            s.append("0")
            prev = 0

        elif(prev == 0):
            # If c == 1 we have to:
            # 1. If also i == n, append 1.
            # 2. else, append 0:

            if(i == n):
                c-= 1
                s.append("1")

            else:
                s.append("0")
                prev = 0

        elif(prev == -1):
            prev = 1
            s.append("1")
    else:
        # General case c > 1:
        # Try to reduce down c.

        if(prev == 1):
            prev = 0
            s.append("0")
            c -= 1


        elif(prev == 0):
            s.append("1")
            prev = 1
            c -= 1

        elif(prev == -1):
            if(c % 2 == 0):
                s.append("0")
                prev = 0
            else:
                s.append("1")
                prev = 1


print("".join(s))
