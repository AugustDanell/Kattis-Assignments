stars = int(input())
x = 2
print("%d:"%stars)
while(x < (stars)):
    y = x-1

    while(y <= x):
        internalStars = stars
        startX = True
        while(internalStars > 0):
            if(startX):
                internalStars = internalStars - x
            else:
                internalStars = internalStars - y
            startX = not startX

            if(internalStars == 0):
                print("%d,%d"%(x,y))
            elif(internalStars < 0):
                break
        y = y+1
    x = x+1