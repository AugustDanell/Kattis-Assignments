def appendPeanoIt(n, s, acc):
    while n > 1:
        acc += 1
        s += "S("
        n-=1
        
    return s + "S(0" + ")"*(acc+1)

def appendPeano(n, s, acc):
    if n == 1:
        return s + "S(0" + ")"*(acc+1)
    else:
        acc += 1
        s += "S("
        return appendPeano(n-1, s, acc)

x = input()
y = input()

if x == "0" or y == "0":
    print(0)
else:
    occurancesX = x.count("S")
    occurancesY = y.count("S")
    #print(appendPeano(occurancesX*occurancesY, "", 0))
    print(appendPeanoIt(occurancesX*occurancesY, "", 0))
