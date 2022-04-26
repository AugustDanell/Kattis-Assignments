# 1. List Trick for input:
l, r = list(map(int, input().split()))

# 2. Check the greatest square peg distance by taking the hypotenuse from the center to the corner points:
center_dist = l/2
hyp = (center_dist**2 + center_dist**2)**0.5

# 3. Check which is greatest, the circle's equidistant radius, or the largest hypothenuse value of the square peg:
if(r > hyp):
    print('fits')
else:
    print('nope')
