diff = int(input())
data = list (input())

first = data.pop(0)
men = 0
women = 0
count = 0

while(len(data) > 0):

    if(abs(men - women) > diff):
        count -= 1
        break

    e = data.pop(0)
    #print(first, e, abs(men-women))


    if(e == first):
        if(e == "M"):
            men += 1
        else:
            women +=1
    else:
        # They are not the same:
        if(e == "M" and men > women):
            women += 1
            first = "M"

        elif(e == "W" and women > men):
            men += 1
            first = "W"

        else:
            # Amount of women = amount of men
            if(e == "W"):
                women +=1
            else:
                men += 1
    count += 1

if(first == "M"):
    men += 1
else:
    women += 1

if(abs(men-women) > diff):
    None
else:
    count += 1

print(count)