# Input
r,f = list(map(int, input().split()))
degreesPerSecond = 180 / r
totalRot = (degreesPerSecond*f)%360

# Check rotation:
if(totalRot >= 90 and totalRot <= 270):
    print("down")
else:
    print("up")
