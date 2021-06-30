def secondClock(s1, s2):
    #print(s1, s2)
    carryOver = 0
    seconds = 0
    while(not (s1 == s2)):
        s1 = s1 + 1
        if(s1 == 60):
            carryOver = 1
            s1 = 0
        seconds = seconds + 1

    return carryOver, seconds


def minuteClock(m1,m2):
    carryOver = 0
    minutes = 0

    while(not m1 == m2):
        m1 = m1 + 1
        if(m1 == 60):
            carryOver = 1
            m1 = 0
        minutes = minutes + 1

    return carryOver, minutes

def hourClock(h1,h2):
    hours = 0

    while(not (h1 == h2)):
        #print(h1, h2)
        h1 = h1 + 1
        if(h1 >= 24):
            h1 = 0

        hours = hours + 1

    return hours

inp1 = input().split(":")
s1 = int(inp1[2])
m1 = int(inp1[1])
h1 = int(inp1[0])

inp2 = input().split(":")
s2 = int(inp2[2])
m2 = int(inp2[1])
h2 = int(inp2[0])


sCarry, seconds = secondClock(s1,s2)
m1 = m1 + sCarry
if(m1 == 60):
    m1 = 0
    h1 = h1 +1

mCarry, minutes = minuteClock(m1,m2)
h1 = h1 + mCarry
if(h1 == 24):
    h1 = 0

hours = hourClock(h1,h2)

#print(hours, minutes, seconds)

h = hours.__str__()
if(len(h) == 1):
    h = "0" + h

m = minutes.__str__()
if(len(m) == 1):
    m = "0" + m

s = seconds.__str__()
if(len(s) == 1):
    s = "0" + s

if(h1 == h2 and m1 == m2 and s1 == s2):
    print("24:00:00")
else:
    print("%s:%s:%s"%(h,m,s))