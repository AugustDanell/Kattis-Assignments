a,b,c,d = list(map(int, input().split()))

mult_op = a*b
problem = True
if(mult_op == c*d):
    print(a, "*", b, "=", c, "*", d)
    problem = False

if(mult_op == c+d):
    print(a, "*", b, "=", c, "+", d)
    problem = False

if(mult_op == c-d):
    print(a, "*", b, "=", c, "-", d)
    problem = False

if(not d == 0):
    if(mult_op == c//d):
        print(a, "*", b, "=", c, "/", d)
        problem = False

add_op = a+b
if(add_op == c*d):
    print(a, "+", b, "=", c, "*", d)
    problem = False

if(add_op == c+d):
    print(a, "+", b, "=", c, "+", d)
    problem = False

if(add_op == c-d):
    print(a, "+", b, "=", c, "-", d)
    problem = False

if(not d == 0):
    if(add_op == c//d):
        print(a, "+", b, "=", c, "/", d)
        problem = False

sub_opp = a-b
if(sub_opp == c*d):
    print(a, "-", b, "=", c, "*", d)
    problem = False

if(sub_opp == c+d):
    print(a, "-", b, "=", c, "+", d)
    problem = False

if (sub_opp == c - d):
    print(a, "-", b, "=", c, "-", d)
    problem = False

if(not d == 0):
    if (sub_opp == c // d):
        print(a, "-", b, "=", c, "/", d)
        problem = False


if(not b == 0):
    div_opp = a // b
    if(div_opp == c*d):
        print(a, "/", b, "=", c, "*", d)
        problem = False

    if(div_opp == c+d):
        print(a, "/", b, "=", c, "+", d)
        problem = False

    if (div_opp == c - d):
        print(a, "/", b, "=", c, "-", d)
        problem = False

    if(not d == 0):
        if (div_opp == c // d):
            print(a, "/", b, "=", c, "/", d)
            problem = False

if(problem):
    print("problems ahead")
