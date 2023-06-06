# 710th Kattis, A Solution To The Problem: https://open.kattis.com/problems/financialplanning

'''
    General Solution: 
    Sort based on ratios, using higher order functions.
    
'''

import math

# 1. Read in the data and create a list where investment[-1] is a ratio
N, target = list(map(int,input().split()))
investments = []
for _ in range(N):
    income,cost = list(map(int,input().split()))
    ratio = income/cost
    investments.append([income, cost, ratio])

# 2. Sort based on highest ratio:
sorting_func = lambda x: x[-1]
sorted_investments = sorted(investments, key = sorting_func, reverse=True)
aggregated_cost, aggregated_income = 0,0
total_days = -1

# 3. Iterate over each investment based on ratios and take only those that improve our time (We could insert a break probably):
for investment in sorted_investments:
    income,cost = investment[0], investment[1]
    days = (target + cost) / income

    if total_days == -1:
        total_days = days
        aggregated_income = income
        aggregated_cost = cost
        continue

    new_days = (target + cost + aggregated_cost)/ (income + aggregated_income)
    if new_days < total_days:
        total_days = new_days
        aggregated_income += income
        aggregated_cost += cost

# 4. Print the result, make use of ceil to make sure that we are not dealing with fractions of a day, 5.712123 etc:
print(math.ceil(total_days))
