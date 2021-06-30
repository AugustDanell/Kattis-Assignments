import math

inp = input()
split = inp.split()

reqArea = float(split[0])
materials = float(split[1])

omkrets = materials
radie = (omkrets/2)/math.pi

area = (radie**2)*math.pi
if(area > reqArea):
    print("Diablo is happy!")
else:
    print("Need more materials!")