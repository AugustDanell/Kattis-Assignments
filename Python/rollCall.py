import sys

# lastname, firstname, fullname, useFullName
def selectionSort(l1, l2, l3,u1):
    length = len(l1)
    for i in range(length):
        minIndex = i
        for j in range(i+1,length):
            if(l1[minIndex] > l1[j]):
                minIndex = j

            if(l1[minIndex] == l1[j]):
                if(l2[minIndex] > l2[j]):
                    minIndex = j

        l1[i], l1[minIndex] = l1[minIndex], l1[i]
        l2[i], l2[minIndex] = l2[minIndex], l2[i]
        l3[i], l3[minIndex] = l3[minIndex], l3[i]
        u1[i], u1[minIndex] = u1[minIndex], u1[i]

    return l1,l2,l3, u1


names = []
fullNames = []
useFullName = []
lastNames = []
for line in sys.stdin:
    data = line.split()
    #print(data)

    if(not names.__contains__(data[0])):
        useFullName.append(False)
    else:
        index = names.index(data[0])
        #names[index] = fullNames[index]
        useFullName[index] = True
        useFullName.append(True)

    names.append(data[0])
    fullNames.append(data[0] + " " + data[1])
    lastNames.append(data[1])


lastNames,names,fullNames,useFullName = selectionSort(lastNames,names,fullNames, useFullName)
finalList = []
for i in range(len(fullNames)):
    if(useFullName[i]):
        #finalList.append(fullNames[i])
        print(fullNames[i])
    else:
        #finalList.append(names[i])
        print(names[i])
#print(finalList)