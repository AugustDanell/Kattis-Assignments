# 0. Function to handle Euclidean Dist:

def euclidean_dist(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5

# 1. Handle the Input with the list-map trick:
olax0, olay0, karix0, kariy0, olax1, olay1, karix1, kariy1 = list(map(int, input().split()))

# 2. Think of this as two linesegments in 2D space. What is the max distance?

''' Consider three possibilities:
    a) The line segments are parallell
    b) The line segments are not paralell and converge
    c) The line segments are not parallell and diverge
    
    Paralell:               Diverging:                   Converging:
    s--------e                   e                      s           e
             | d1              . |                      | .       . |
    s--------e               .   |                      |   .   .   |
                           .     |                   d0 |     .     | d1
                         s       | d1                   |   .   .   | 
                           .     |                      | .       . |
                             .   |                      s           e
                               . |
                                 e
    
    Let d0 be the distance between the resp starting points and d1 be the distance between resp endpoint.
    Max(d0, d1) will give the global max because regardless of which case as seen above one of these distances will hold the global largest distance. 
    
'''

# The two endpoints:
d0 = euclidean_dist(olax0, olay0, karix0, kariy0)
d1 = euclidean_dist(olax1, olay1, karix1, kariy1)

print(max(d0, d1))
