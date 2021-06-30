data = input().split()
m = int(data[0])
a = int(data[1])
b = int(data[2])
c = int(data[3])

# A and b try to spread out their choices
doubleChoice = a+b-m
if(doubleChoice <= 0):
    # No menu has been selected twice, so it is possible
    print("possible")

elif(m-doubleChoice >= c):
    print("possible")

else:
    print("impossible")
