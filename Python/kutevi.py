# Kutevi
# Basically this problem is all about linear combinations. The time limit exceeded stats seem small so maybe we can
# brute force it. Multiplication is a commutative operation. We could do an ugly solution with having a dictionary as 
# a global variable. We can access this to do lookups in constant time (average case). We can then use recursion to 
# always check a combination of every angle. When we come across an angle that we have already use we quit the recursion.

angle_dictionary = {}
ans = False
angles, select = list(map(int, input().split()))
known_angles = list(map(int, input().split()))
asked_angles = list(map(int, input().split()))

def recursion(angle, angle_to_solve, first_recursion = False):
    global angle_dictionary
    global known_angles
    global ans

    # Base Case:
    if(angle_dictionary.__contains__(angle)):
        return
    elif(angle == angle_to_solve and not first_recursion):
        ans = True
        return
    else:
        # Recursive case:
        if(not first_recursion):
            angle_dictionary[angle] = True

        for next_angle in known_angles:
            recursion((angle+next_angle)%360, angle_to_solve, first_recursion = False)

def start_recursion(l, angle_to_solve):
    for angle in l:
        recursion(angle, angle_to_solve)


# Start a recursion on all starting angles: 
for angle_to_solve in asked_angles:
    start_recursion(known_angles, angle_to_solve)

    if(ans):
        print("YES")
    else:
        print("NO")

    # Reset Global Var
    angle_dictionary = {}
    ans = False
