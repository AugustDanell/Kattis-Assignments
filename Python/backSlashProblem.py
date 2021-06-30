import sys

def isEscapeChar(c):
    a = ord(c)
    if(a >= 91 and a <= 93):
        return True
    if(a >= 33 and a <= 42):
        return True
    return False

def fixString(s):
    l = list(s)
    insertions = 0
    for i in range(len(s)):
        if(isEscapeChar(s[i])):
            l.insert(i + insertions, "\\")
            insertions += 1

    return "".join(l)


for line in sys.stdin:
    level = int(line)
    message = input()

    for i in range(level):
        message = fixString(message)

    print(message)