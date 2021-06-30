geneticString = ""
while(not geneticString == "0"):
    same = 0
    removal = 0
    inserts = 0

    geneticString = input()
    if(geneticString == "0"):
        break

    data = geneticString.split()
    length = len(data[0])

    noChanges = data[0]
    removeOne = []
    for i in range(length):
        s = (data[0])[0:i] + (data[0])[i+1:]
        removeOne.append(s)

    insertOne = []
    for i in range(length):
        A = (data[0])[0:i] + "A" + (data[0])[i:]
        G = (data[0])[0:i] + "G" + (data[0])[i:]
        C = (data[0])[0:i] + "C" + (data[0])[i:]
        T = (data[0])[0:i] + "T" + (data[0])[i:]

        insertOne.append(A)
        insertOne.append(G)
        insertOne.append(C)
        insertOne.append(T)

    insertOne.append(data[0] + "A")
    insertOne.append(data[0] + "G")
    insertOne.append(data[0] + "C")
    insertOne.append(data[0] + "T")

    lengthLong = len(data[1])
    for i in range(lengthLong-length+2):
            remSubstring  = (data[1])[i:i+length-1]


            sameSubstring = (data[1])[i:i+length]
            plusSubstring = (data[1])[i:i+length+1]

            #print(plusSubstring)

            #print(remSubstring)
            #print(sameSubstring)
            #print(plusSubstring)

            if (sameSubstring == noChanges):
                same = same + 1

            if(remSubstring in removeOne):
                removal = removal + 1

            if(plusSubstring in insertOne):
                inserts = inserts + 1


    print(same, removal, inserts)