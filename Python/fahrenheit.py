#Problem ID: temperatureconfusion
def gcd(n,d):
    if(n == 0):
        return "0/1"

    #print(n) #-360
    #print(d) #   9

    foundD = True
    while(foundD):
        foundD = False
        for i in range(d):
            c = i+1
            if(not(c == 1) and (n%c == 0) and (d%c == 0)):
                #print("entered")
                foundD = True
                n = int(n/c)
                d = int(d/c)
                #print(d)
                break

    return "%d/%d"%(n,d)


f = (input())
data = f.split("/")
#print(data)

numerator = int(data[0])
denominator = int(data[1])

inner = numerator - (32*denominator)
outer = 5/(9*denominator)

fullD = 9*denominator
fullN = 5*inner

print(gcd(fullN,fullD))

