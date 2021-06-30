def fac(n):
    if(n == 1):
        return 1
    elif(n >= 10):
        return 10**(6)
    else:
        return fac(n-1)*n

gifts = int(input())
s = 0.0

six = 1. - 1/2 + 1/6 - 1/24 + 5/720
if(gifts == 1):
    print(1)
elif(gifts == 2):
    print(0.5)
elif(gifts == 3):
    print(2/3)
elif(gifts == 4):
    print(1. - 1/2 + 1/6 - 1/24)
elif(gifts == 5):
    print(1. - 1/2 + 1/6 - 1/24 + 1/120)
elif(gifts == 6):
    print(1. - 1/2 + 1/6 - 1/24 + 5/720)
elif(gifts == 7):
    print(six + 1/5040)
elif(gifts == 8):
    print(six + 1/5040 - 1/fac(8))
elif(gifts == 9):
    print(six + 1/5040 - 1/fac(8) + 1/fac(9))
elif(gifts == 10):
    print(six + 1/5040 - 1/fac(8) + 1/fac(9) - 1/fac(10))
else:
    print(six + 1/5040 - 1/fac(8) + 1/fac(9) - 1/fac(10) + 1/fac(11))