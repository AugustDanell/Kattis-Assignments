cases = int(input())

for j in range(cases):

    dic = {}
    entries = int(input())
    for i in range(entries):
        order = input().split()
        name = order[0]
        quantity = int(order[1])

        if(dic.__contains__(name)):
            dic[name] += quantity
        else:
            dic[name] = quantity

    #values = sorted(dic.values(), reverse = True)
    items = sorted(dic.items(), key = lambda x:x[1])
    items.reverse()
    #print(items)
    #print(len(items))

    completeList = []
    prev = items[0][1]
    l = [items[0][0]]

    for i in range(1,len(items)):
            current = items[i][1]
            if(prev == current):
                    l.append(items[i][0])
            else:
                completeList.append(l)
                l = [items[i][0]]

            prev = current

    if(len(l) > 0):
        completeList.append(l)

    ## Printing phase
    print(len(dic))
    for i in range(len(completeList)):
        completeList[i].sort()
        for j in range(len(completeList[i])):
            item = completeList[i]
            print(item[j], dic[item[j]])