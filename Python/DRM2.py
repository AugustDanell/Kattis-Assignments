def rotateChar(c,r):
    v = (ord(c) + r - 65) % 26
    return chr(v+65)

def alphaVal(c):
    return ord(c)- 65

def messageValue(m):
    v = 0
    for i in m:
        v += (ord(i)) - 65

    return v

message = input()
length = len(message)//2
first = list(message[:length])
second = list(message[length:])

r1 = messageValue(first)
r2 = messageValue(second)

# Rotate first and second string
# AND use second as key to first:
for i in range(length):
    first[i] = rotateChar(first[i], r1)
    second[i] = rotateChar(second[i], r2)

    k = alphaVal(second[i])
    first[i] = rotateChar(first[i], k)


print("".join(first))
# String length is even!


#print(messageValue("ABCZ")) # OK
#print(rotateChar("A",26)) # prob ok

