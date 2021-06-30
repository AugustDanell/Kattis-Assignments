def generateList(roof):
    a = 0
    l = []
    while(a**3 <= roof):
        l.append(a**3)
        a += 1

    return l

def naiveMethod(roof):
    l1 = generateList(roof)
    #l2 = generateList(roof)
    length = len(l1)
    ways = 0

    for i in range(length):
        for j in range(i, length):
            if(l1[i] + l1[j] == roof):
                ways += 1
                #print(l1[i], l1[j])
                if(ways == 2):
                    return roof

    return -1

roof = int(input())

if(roof < 1729):
    print("none")
else:
    ans = 0
    while(1):
        ans = naiveMethod(roof)
        if(ans == -1):
            roof -= 1
        else:
            break

    print(ans)