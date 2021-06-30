# Solution to Conformity
def max(l):
    max = 0
    for i in range(len(l)):
        if(l[i] > max):
            max = l[i]
    return max

n = int(input())
courseList =[]
attendeeList = []

for i in range(n):
    data = input()
    split = data.split()
    internalList = []
    courseConcat = ""
    for j in range (5):
        course = (int(split[j]))
        internalList.append(course)

    internalList.sort()
    for j in range (5):
        courseConcat = courseConcat + internalList[j].__str__()

    if(courseList.__contains__(courseConcat)):
        index = courseList.index(courseConcat)
        attendeeList[index] = attendeeList[index] + 1
    else:
        courseList.append(courseConcat)
        attendeeList.append(1)

m = max (attendeeList)
s = 0
for i in range(len(attendeeList)):
    if(attendeeList[i] == m):
        s = s + attendeeList[i]

print(s)