import math

# Single Variable Calculus to derive a solution formula:
# Let v(x) = (c1 - 2x)(c2-2x)x = 4x^3 - 2x^2(c1 + c2) + x*c1c2. [Volume function].
# Derive v'(x) = 12x^2 - 4x(c1 + c2) + c1c2. [Derivation for maxima].
# Normalize v'(x) = x^2 - 4/12x(c1+c2) + 1/12 c1c2. [Norm with regards to x^2 coefficient].
# PQ formula to solve for x^2:

# 1. (Base): x = 1/6*c1*c2
# 2. (P/M): sqrt((1/6)^2 * c1^2 * c2^2 -)

def volume(c1, c2, x):
    if(c1 - 2*x < 0 or c2 - 2*x < 0 or x < 0):
        return 0

    area = (c1 - 2*x)*(c2-2*x)
    height = x

    return area * height

def get_extreme_points(c1, c2):
    base = 1/6 * (c1 + c2)
    root_expr = math.sqrt((1/6 * (c1 + c2))**2 - (1/12 *c1*c2))

    return base + root_expr, base - root_expr

for i in range(int(input())):
    c1, c2 = list(map(int, input().split()))
    p1, p2 = get_extreme_points(c1, c2)
    max_vol = max(volume(c1,c2,p1), volume(c1, c2, p2))
    print(max_vol)
