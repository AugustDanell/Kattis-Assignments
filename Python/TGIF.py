# Problem ID: TGIF

dayMap = {}
dayMap["MON"] = 1
dayMap["TUE"] = 2
dayMap["WED"] = 3
dayMap["THU"] = 4
dayMap["FRI"] = 5
dayMap["SAT"] = 6
dayMap["SUN"] = 7

monthMap = {}
monthMap["JAN"] = 1
monthMap["FEB"] = 2
monthMap["MAR"] = 3
monthMap["APR"] = 4
monthMap["MAY"] = 5
monthMap["JUN"] = 6
monthMap["JUL"] = 7
monthMap["AUG"] = 8
monthMap["SEP"] = 9
monthMap["OCT"] = 10
monthMap["NOV"] = 11
monthMap["DEC"] = 12

monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Since we start at the first day of Jan the first day does not count.
# Therefore we need to subtract one later on:

data = input().split()
month = monthMap[data[1]]
days = int(data[0]) - 1 # See above

startDay = dayMap[input()]
days += startDay - 1

for i in range(month-1):
    days += monthList[i]

#print((days%7) + 1)

weekday = ((days%7) + 1)

if(month > 2):
    if(weekday == 4 or weekday == 5):
        print("not sure")
    else:
        print(":(")
else:
    if(weekday == 5):
        print("TGIF")
    else:
        print(":(")
