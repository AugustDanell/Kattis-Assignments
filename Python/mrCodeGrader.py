def hyphenList(l):
    str = ""
    prevItem = -100
    hyphen = False

    for item in l:
        if(prevItem +1 == item):
            hyphen = True
        else:
            if(hyphen):
                str = str[:-2]
                str += "-{1}, {0}, ".format(item, prevItem)
            else:
                str += "{0}, ".format(item)
            hyphen = False

        prevItem = item

    if hyphen:
        str = str[:-2]
        str += "-{0}".format(prevItem)

    strl = str.split(",")
    if strl.__contains__(" "):
        strl.remove(" ")

#    print(strl)
    if len(strl) > 1:
        strl.insert(len(strl) - 1, " and")
        for i in range (len(strl)-3):
                strl[i] += ","

    return "".join(strl)


lines, errors = list(map(int, input().split()))
errorList = list(map(int, input().split()))
correctList = [i for i in range(1, lines+1) if not i in errorList]



print("Errors:", hyphenList(errorList))
print("Correct:", hyphenList(correctList))
