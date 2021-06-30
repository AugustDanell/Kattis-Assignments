def parseAndSort(l):
    for i in range(len(l)):
        l[i] = float(l[i])

    return sorted(l)

while(1):
    inp = input()
    if(inp == "0 0 0.0"):
        break

    data = inp.split()
    nx = int(data[0])
    ny = int(data[1])
    w = float(data[2])

    isOk = True
    #Horisontal cuts:
    horisontalData = input().split()
    location = 0.0

    horisontalData = parseAndSort(horisontalData)
    for i in range(len(horisontalData)):
        cut = (horisontalData[i])
        if(location + w < cut):
            isOk = False
            break
        else:
            location = cut

    if(location + w/2 < 75.0):
        isOk = False

    #Vertical cuts
    verticalData = input().split()
    if(isOk):
        verLocation = 0.0
        verticalData = parseAndSort(verticalData)
        for i in range(len(verticalData)):
            cut = float(verticalData[i])
            if(verLocation + w < cut):
                isOk = False
                break
            else:
                verLocation = cut

        if(verLocation + w/2 < 100.0):
            isOk = False

    if(isOk):
        print("YES")
    else:
        print("NO")
