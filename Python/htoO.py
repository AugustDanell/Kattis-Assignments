def extractAtoms(dic, inputData):
    compoundString = inputData[0]
    compound = ""
    copies = ""
    lastAlpha = False

    for i in range(len(compoundString)):
        #print(compoundString[i])
        if (compoundString[i].isalpha()):

            # Base case:
            if (i == 0):
                lastAlpha = True
                compound = compoundString[0]
                continue

            if (lastAlpha):
                if (dic.__contains__(compound)):
                    dic[compound] += 1 * multiplier
                else:
                    dic[compound] = 1 * multiplier
            else:
                numbers = int(copies)
                if (dic.__contains__(compound)):
                    dic[compound] += numbers * multiplier
                else:
                    dic[compound] = numbers * multiplier

            compound = compoundString[i]
            copies = ""
            lastAlpha = True
        else:
            copies += compoundString[i]
            lastAlpha = False

    if (not copies == ""):
        numbers = int(copies)
        if (dic.__contains__(compound)):
            dic[compound] += numbers * multiplier
        else:
            dic[compound] = numbers * multiplier
    else:
        if (dic.__contains__(compound)):
            dic[compound] += 1 * multiplier
        else:
            dic[compound] = 1 * multiplier

    return dic

dic = {}
dic2 = {}

inputData = input().split()
multiplier = int(inputData[1])

# Phase one: Extract atoms:

dic = extractAtoms(dic, inputData)
multiplier = 1
dic2 = extractAtoms(dic2, input().split())

#print(dic)
#print(dic2)

# Phase two - see how many of these atoms fit into what we need:
min = 300000000000
keys = dic2.keys()

for key in keys:
    if(not dic.__contains__(key)):
        min = 0
        break
    else:
        local = dic[key] // dic2[key]
        if(local < min):
            min = local

print(min)
