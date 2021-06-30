# Generally we should use modulo and division to take out a rest
# a digit but since the sample size is small we use string

def badDigitProd(a):
    s = a.__str__()

    prod = 1
    for i in s:
        x = int(i)
        if(x > 0):
            prod *= x

    return prod


number = int(input())
while(number > 9):
    number = badDigitProd(number)
print(number)