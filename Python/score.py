# 300
def clockToFlatTime(s):
    s2 = s.split(":")
    return (int(s2[0])*60 + int(s2[1]))

def flatToClockTime(t):
    s1 = 0
    while(t >= 60):
        t-= 60
        s1 += 1

    s2 = t

    return s1.__str__() + ":" + s2.__str__()

Home = 0 # Starting scores for the teams:
timeHome = 0
Away = 0
timeAway = 0
lead = 0 # If lead == 1, home is leading, if lead == 0, tie, -1 away is leading.
lastH = 0
lastA = 0
time = 0
scoresA = 0
scoresH = 0


queries = int(input())
for i in range(queries):
    query = input().split()
    team = query[0]
    score = int(query[1])
    time = clockToFlatTime(query[2])

    if(team == "A"):
        Away += score
    else:
        Home += score

    # Case one TIE. It is a tie from either H lead or A lead:
    if(Away == Home):
        if(lead == 1):
            timeHome += time - lastH
            lastH = time
        elif(lead == -1):
            timeAway += time - lastA
            lastA = time

        lead = 0 # Set lead to tie.

    # Case two HOME, Home team takes the lead:
    if(Home > Away):
        if(lead == 1):
            # Do nothing
            None
        elif(lead == 0):
            lastH = time # EX1: lasth = 13
        else:
            #lead = -1:
            timeAway += time - lastA
            lastH = time

        lead = 1

    # Case three AWAY, away team takes the lead:
    if(Away > Home):
        if(lead == 1):
            timeHome += time - lastH
            lastA = time
        elif(lead == 0):
            lastA = time
        else:
            # Do nothing
            None

        lead = -1

    #print("TEST:", timeAway, timeHome, lead, Away, Home)

# Last outside modifications:
time = clockToFlatTime("32:00")
if(lead == 1):
    timeHome += time - lastH
elif(lead == -1):
    timeAway += time - lastA

isHomeWin = True
if(Away > Home):
    isHomeWin = False

if(isHomeWin):
    print("H", end = " ")
else:
    print("A", end = " ")

o1 = flatToClockTime(timeHome)
o2 = flatToClockTime(timeAway)
if(o1[-2] == ":"):
    temp = o1[-1]
    o1 = o1[:-1] + "0" + temp

if(o2[-2] == ":"):
    temp = o2[-1]
    o2 = o2[:-1] + "0" + temp

print(o1, end = " ")
print(o2, end = " ")

