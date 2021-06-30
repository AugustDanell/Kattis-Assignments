# Just check for duplicates in the text.
text = input()
list = []
foundDup = False

for c in text:
    if(list.__contains__(c)):
        foundDup = True
        break
    else:
        list.append(c)

if(foundDup):
    print(0)
else:
    print(1)