friends = int(input())
for i in range(friends):
    date, month = input().split()
    date = int(date)

    if((date >= 21 and month == "Mar") or (date <= 20 and month == "Apr")):
        print("Aries")
    elif ((date >= 21 and month == "Apr") or (date <= 20 and month == "May")):
        print("Taurus")
    elif ((date >= 21 and month == "May") or (date <= 21 and month == "Jun")):
        print("Gemini")
    elif ((date >= 22 and month == "Jun") or (date <= 22 and month == "Jul")):
        print("Cancer")
    elif ((date >= 23 and month == "Jul") or (date <= 22 and month == "Aug")):
        print("Leo")
    elif ((date >= 23 and month == "Aug") or (date <= 21 and month == "Sep")):
        print("Virgo")
    elif ((date >= 22 and month == "Sep") or (date <= 22 and month == "Oct")):
        print("Libra")
    elif ((date >= 23 and month == "Oct") or (date <= 22 and month == "Nov")):
        print("Scorpio")
    elif ((date >= 23 and month == "Nov") or (date <= 21 and month == "Dec")):
        print("Sagittarius")
    elif ((date >= 22 and month == "Dec") or (date <= 20 and month == "Jan")):
        print("Capricorn")
    elif ((date >= 21 and month == "Jan") or (date <= 19 and month == "Feb")):
        print("Aquarius")
    elif ((date >= 20 and month == "Feb") or (date <= 20 and month == "Mar")):
        print("Pisces")
