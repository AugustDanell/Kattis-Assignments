data = input().split()
B0 = int(data[0])       # When A = 0
stepB = int(data[1])    # Stepping size for B, relative A.
D = stepB -1

#  D is the growth factor:
#  stepA is always = 1, so if stepB = 2
#  and B(0) = 5, B(-1) = 3, A(-1) = -1..
#  We can call this the Differance D instead
#  seen above. In this example we get:
#  D(-1) = |3 -- 1| = 4
#  D(-2) = 3
#  ... D(-5) = 0

if(not B0 == 0 and D == 0):
    print("IMPOSSIBLE")
elif(B0 == 0 and D == 0):
    print("ALL GOOD")
elif(D > 0 and B0 > 0):
    print(-abs(B0/D))
else:
    print(abs(B0/D))