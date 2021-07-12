def numerize(s):
    if s == "South":
        return 1
    elif s == "West":
        return 2
    elif s == "North":
        return 3
    elif s == "East":
        return 0

start, end, opp = map(lambda x: numerize(x),input().split())
left = [-1,3]
right = [1,-3]

if(abs(start-end) == 2 and (start - opp in right)):
    print("Yes")

elif((start-end in left) and ((abs(start-opp) == 2) or (start-opp in right))):
    print("Yes")

else:
    print("No")
