M = 4
Y = 2018
found = False

askYear = int(input())
if(askYear == 2018):
    found = True

while(Y < askYear):
    if(M == 12):
        Y = Y+1
        M = 0

    Y = Y + 2
    M = M+2

    if(Y == askYear):
        found = True
        break

if(found):
    print("yes")
else:
    print("no")