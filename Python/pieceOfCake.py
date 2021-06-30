inp = input()
split = inp.split()

n = int(split[0])
h = int(split[1])
v = int(split[2])

side1 = 0
side2 = 0
if((n-h) > h):
    side1 = n-h
else:
    side1 = h

if((n-v) > v):
    side2 = n-v
else:
    side2 = v

print(4*side1*side2)