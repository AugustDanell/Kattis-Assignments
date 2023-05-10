# A solution to the problem: https://open.kattis.com/problems/bestbefore

def numeric_value(day, month, year):
    return day + month*100 + year*10000

def leap_year(year):
    if not year%4 == 0:
        return False
    if year%100 == 0 and not year%400 == 0:
        return False
    return True

assert leap_year(2000)
assert not leap_year(2100)
assert leap_year(2012)

# Checks the validity and value of an assignment. If unvalid, return -1. Else return a numeric value >= 0:
def value_check(day, month, year):
    long_months = [1,3,5,7,8,10,12]
    short_months = [4,6,9,11]
    #print(day, month, year)

    if year > 2999 or day <= 0 or month <= 0:
        return -1
    elif month == 2 and day == 29 and leap_year(year):
        return numeric_value(day, month, year)
    elif month <= 12 and day <= 28:
        return numeric_value(day, month, year)
    elif month in long_months and day <= 31:
        return numeric_value(day, month, year)
    elif month in short_months and day <= 30:
        return numeric_value(day, month, year)

    return -1

assert not value_check(28, 2, 2013) == -1
assert not value_check(29, 2, 2012) == -1
assert value_check(29, 2, 2013) == -1


date_str = input()
l = list(map(int,date_str.split("/")))
earliest_date = -1
best_list = []

# Test every solution:
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            continue
        for k in range(len(l)):
            if k == j or k == i:
                continue

            adjusted_year = l[k]
            if adjusted_year < 2000:
                adjusted_year += 2000

            local_value = value_check(l[i], l[j], adjusted_year)
            if (earliest_date == -1 or local_value < earliest_date) and (not local_value == -1):
                earliest_date = local_value
                best_list = [adjusted_year, l[j], l[i]]

# Add Padding:
for i in range(len(best_list)):
    if best_list[i] < 10:
        best_list[i] = "0" + str(best_list[i])

if earliest_date == -1:
    print("{0} is illegal".format(date_str))
else:
    print("{0}-{1}-{2}".format(best_list[0], best_list[1], best_list[2]))
