# 0. Function to handle Euclidean Dist:

def euclidean_dist(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5

# 1. Handle the Input with the list-map trick:
olax0, olay0, karix0, kariy0, olax1, olay1, karix1, kariy1 = list(map(int, input().split()))

# 2. Think of this as two linesegments in 2D space. What is the max distance?

''' Consider two possibilities:
    a) The line segments are parallell
    b) The line segments are not paralell
    
    a: If they are paralell the max distance can be any two points.
    b: If they are not paralell the max distance should be at the end points. Why?
    Because if the two lines converge / cross each other the max distance will
    decrease until the crossing and then increase ever more. As such either the start point
    or the final point will hold the max distance.
    
    If the two lines from the start are diverging then the endpoints will be the max
    distance of the two (obviously). 
'''

# The two endpoints:
d0 = euclidean_dist(olax0, olay0, karix0, kariy0)
d1 = euclidean_dist(olax1, olay1, karix1, kariy1)

print(max(d0, d1))
