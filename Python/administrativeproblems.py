# A solution to the problem: https://open.kattis.com/problems/administrativeproblems

import math

# 0. Read in testcases: 
testcases = int(input())
for _ in range(testcases):
    cars = {}
    operatives = {}
    money_map = {}

    # 1. Read in car data for the test case and save it to a hashmap:
    n, m = list(map(int, input().split()))
    for _ in range(n):
        car = input().split()
        cars[car[0]] = [int(car[1]), int(car[2]), int(car[3])]

    # 2. Iterate over operations and deal with every case:
    for _ in range(m):
        time, operative, operation, car = input().split()

        # Skip over inconsitent operatives, we dont need to consider them anyway:
        if operatives.__contains__(operative) and operatives[operative] == "INCONSISTENT":
            continue

        # A. Cover valid Pickup of a car and inconsistent Returns/Accidents:
        if not operatives.__contains__(operative) or operatives[operative] == None:
            if operation == "a" or operation == "r":
                operatives[operative] = "INCONSISTENT"
            else:
                operatives[operative] = car
                car_checkout_price = cars[car][1]

                if money_map.__contains__(operative):
                    money_map[operative] += car_checkout_price
                else:
                    money_map[operative] = car_checkout_price

        # B. Cover accident of valid car and debt the operative:
        elif operation == "a":
            severity = int(car) / 100
            towed_car = cars[operatives[operative]][0]
            repair_price = math.ceil(severity * towed_car - (1/1e6)) # Small subtract sum to avoid rounding errors

            if not money_map.__contains__(operative):
                money_map[operative] = repair_price
            else:
                money_map[operative] += repair_price

        # C. Cover a valid return of a car and pop the operative from the owner list:
        elif operation == "r":
            kilometers_drive = int(car)
            price_per_km = cars[operatives[operative]][2]
            money_map[operative] += kilometers_drive * price_per_km
            operatives[operative] = None

        # D. Cover invalid pickup of a second car:
        elif operation == "p":
            operatives[operative] = "INCONSISTENT"
    
    # 3. Iterate over the operators sorted lexiographically:
    sorted_operators = sorted(operatives.keys())
    for operator in sorted_operators:
        
        # 4. If an operator has either a car or the label "INCONSISTENT" that means that they are just that. Print inconsistent ones and the debt of the consistent:
        if (operatives[operator] == None):
            print("{0} {1}".format(operator, money_map[operator]))
        else:
            print("{0} INCONSISTENT".format(operator))
