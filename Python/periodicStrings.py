def multiple(a,b):
    if(a%b == 0):
        return True
    return  False

s = input()
length = len(s)

min = 101
for i in range(1, int(length/2) + 1):
    if(not multiple(length,i)):
        continue

    prevSub = s[:i]
    isNotCyclic = False
    for j in range(length-i):
        sub = s[j*i:(j+1)*i]
        if(sub == ""):
            break

        if(not sub == prevSub):
            isNotCyclic = True
           # print("breaking: ", sub, prevSub)
            break


        #print(sub, prevSub)
        prevSub = sub[-1] + sub[:-1]

    if(isNotCyclic):
        continue
    else:
        if(i < min):
            min = i

if(min == 101):
    print(length)
else:
    print(min)