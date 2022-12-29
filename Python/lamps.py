H, P = list(map(int, input().split()))

Clow = 60
Chigh = 5
day = 0
hours = 0

while Chigh < Clow:
    hours += H
    day += 1
    Chigh += (49*H*P)/100000
    if(hours > 1000):
        Chigh += 5
        hours -= 1000

print(day)
