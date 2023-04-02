# A solution to the problem: https://open.kattis.com/problems/trilemma

import math
def euclidean_dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def calculate_area(x1,y1,x2,y2,x3,y3):
    return (1/2)*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

# 0. Read in testcases:
testcases = int(input())
for i in range(testcases):

    # 1. Read in the points of the triangle, initiate the sides and create a prestring as a format string (always used no matter what kind of triangle):
    pre_string = "Case #{0}:".format((i+1))
    x1,y1,x2,y2,x3,y3 = list(map(int,input().split()))
    l12 = euclidean_dist(x1,y1,x2,y2)
    l13 = euclidean_dist(x1,y1,x3,y3)
    l23 = euclidean_dist(x2,y2,x3,y3)

    # 2. Attempt to Disqualify degenerate triangles, i.e, area = 0:
    area = calculate_area(x1,y1,x2,y2,x3,y3)
    if area == 0:
        print(pre_string, "not a triangle")
        continue

    # 3. Calculate the angles of the triangle:
    angular_str = ""
    A = math.degrees(math.acos((l13 **2 + l23**2 - l12**2) / (2*l13*l23)))
    B = math.degrees(math.acos((l12 **2 + l23**2 - l13**2) / (2*l12*l23)))
    C = math.degrees(math.acos((l12 **2 + l13**2 - l23**2) / (2*l12*l13)))
    
    # 4. Fix rounding problem, for example if an angle becomes 90.000000001 (should be 90 and right angle)
    A = round(A, 8)
    B = round(B, 8)
    C = round(C, 8)
    
    # 5. Classify the angle and save a string to be outputted as part of a format string:
    if A == 90 or B == 90 or C == 90:
        angular_str = "right"
    elif A > 90 or B > 90 or C > 90:
        angular_str = "obtuse"
    else:
        angular_str = "acute"
    angular_str += " triangle"

    # 6. Classify the lengths and append message accordingly, to length_str:
    length_str = ""
    if l12 == l13 or l12 == l23 or l13 == l23:
        length_str = "isosceles"
    else:
        length_str = "scalene"
    
    # 7. Print the substrings as part of a format string for the Kattis Output:
    print("{0} {1} {2}".format(pre_string, length_str, angular_str))
