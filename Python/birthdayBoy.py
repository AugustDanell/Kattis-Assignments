# Problem Description: https://open.kattis.com/problems/birthdayboy


# A function that transforms (day, month) -> days
def dateToDays(d, m):
    table = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    totalDays = 0
    for i in range(1, m):
        totalDays += table[i]
    totalDays += d
    return totalDays

# A reverse function that transforms days -> (d, m):
def dayToDate(days):
    table = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    month = 1
    while(days > table[month]):
        days -= table[month]
        month += 1

    monthStr = str(month)
    dayStr = str(days)
    if(len(monthStr) == 1):
        monthStr = "0" + monthStr
    if(len(dayStr) == 1):
        dayStr = "0" + dayStr

    return "{0}-{1}".format(monthStr, dayStr)

# A function that calculates the distance from the start:
def daysAfterStart(day):
    start = dateToDays(28, 10)
    diff = day-start
    if diff >= 0:
        return diff
    else:
        return 365 + diff

if __name__ == "__main__":
    
    # 1. Do some inputs:
    N = int(input())
    dayMap = {}
    for _ in range(N):
        person, date = input().split()
        month, day = date.split("-")
        totalDays = dateToDays(int(day), int(month))
        dayMap[totalDays] = True

    # 2. Create some global flags for best day / best answer:
    bestAns = -1
    bestDay = None
    days = [x for x in range(1,365+1)]
    
    # 3. Iterate over every day:
    for i in range(len(days)):
        day = days[i]
        dist = 0
        
        # 4. Calculate the local score for that day:
        for j in range(365):
            nextDay = days[i-j]
            if nextDay in dayMap:
                break
            else:
                dist += 1
        
        # 5. Check to see if the local score beats the global or if we are closer to start:
        if dist > bestAns or (dist == bestAns and daysAfterStart(day) < daysAfterStart(bestDay)):
            bestDay = day
            bestAns = dist
    
    # 6. Convert best day back into a date:
    bestDate = dayToDate(bestDay)
    
    # 7. Print the best date:
    print(bestDate)
