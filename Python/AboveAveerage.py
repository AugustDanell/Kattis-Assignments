def calcAvg(n, list):
    sum = 0.
    for i in range(n):
        sum = sum + int(list[i])
    return (sum/n)

cases = int(input())
for i in range(cases):
    data = input()
    split = data.split()
    people = int(split[0])
    above = 0.
    average = calcAvg(people, split[1:])


    for j in range(people):
        if(int(split[j+1]) > average):
            above = above + 1.

    percentage = (above/people).__round__(5)*100

    print("%2.3f%%" % (percentage))