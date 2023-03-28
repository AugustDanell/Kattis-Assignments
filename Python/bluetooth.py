# A sloppy solution to the problem: https://open.kattis.com/problems/bluetooth

# 1. Take in input and initiate teeth on upper and lower jaw:
upperOrder = ["8+", "7+", "6+", "5+", "4+", "3+", "2+", "1+", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8"]
lowerOrder = (" ".join(upperOrder).replace("+", "-")).split(" ")
problems = int(input())
lower = {}
upper = {}
leftBroken = False
rightBroken = False

# 2. Read in in tand problems. Immediately disqualify a side if it has a broken tooth, else if m is passed in, we remove the tooth:
for _ in range(problems):
    spot, condition = input().split()
    if condition == "m":
        if upperOrder.__contains__(spot):
            upperOrder.remove(spot)
        elif lowerOrder.__contains__(spot):
            lowerOrder.remove(spot)

    if condition == "b":
        if spot[0] == "-" or spot[0] == "+":
            leftBroken = True
        else:
            rightBroken = True

# 3. Lastly we iterate over two pairs. If there exist a pair that is both right hand side, or left hand side, we mark of the respective boolean:
left,right = False, False
for t_upper in upperOrder:
    for t_lower in lowerOrder:
        if t_upper[0] == "+" and t_lower[0] == "-":
            left = True
        elif t_upper[1] == "+" and t_lower[1] == "-":
            right = True

# 4. We compute two booleans for output. The side are valid if they have atleast on tooth in both lower and upper and no broken teeth:
left_valid = not leftBroken and left
right_valid = not rightBroken and right

# 5. Based on the result of left_valid and right_valid we print out:
if left_valid:
    print(0)
elif right_valid:
    print(1)
else:
    print(2)
