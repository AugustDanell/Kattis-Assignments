def failCheck(s):
    isOk = True
    for i in s[1:]:
        if(ord(i) < 97):
            isOk = False
            break
    return isOk

## START
data = input()
split = data.split()

problems = int(split[0])
cases = int(split[1])
points = problems

problemList = []
for i in range(problems*cases):
    problemList.append(input())

failedSet = False

for i in range(problems*cases):
    if(not failedSet and not (failCheck(problemList[i]))):
        failedSet = True
        #print(i+1)
        points = points -1

    if((i+1) % cases == 0):
        failedSet = False


print(points)