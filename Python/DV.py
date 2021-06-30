def encryptForward(c, k):
    s1 = ord(c) - 65
    s2 = ord(k) - 65

    f = (s1 + s2)%26
    return chr(f+65)

def encryptBackward(c, k):
    s1 = ord(c) - 65
    s2 = ord(k) - 65

    f = ((s1 - s2)%26)
    return chr(f + 65)

s = input()
key = input()
o = []

for i in range(len(s)):
    c = s[i]
    k = key[i]

    if(i % 2 == 0):
        o.append(encryptBackward(c,k))
    else:
        o.append(encryptForward(c,k))

print("".join(o))

