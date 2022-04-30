''' Solution Idea:
    Having been thinking about this problem I think the best solution would be to make it such that we are focusing more on the top row than on the actual piece and its representation. Iterating through every colomn to see if a fit can be made. I implemented some assertions to test the code, simply deactiviating the kattis flag will run the tests instead. I also made a dictionary that take functions as values so when a user inputs a number theirs will be the function corrosponding to the piece of choice. That piece is then fitted according to the line called top row. We iterate through each column and try to fit every rotation on every column basically. 

'''

# TESTS:
def run_tests():
    try:
        test = 1
        real_answer = 7
        ans = fit_piece(1, [0, 0, 0, 0, 0])
        assert (ans == real_answer)

        test = 2
        real_answer = 4
        ans = fit_piece(2, [0, 0, 0, 0, 0])
        assert (ans == real_answer)

        test = 3
        real_answer = 2
        ans = fit_piece(3, [1, 0, 1, 0, 1])
        assert (ans == real_answer)

        test = 4
        real_answer = 2
        ans = fit_piece(4, [1, 0, 1, 0, 1])
        assert (ans == real_answer)

        test = 5
        real_answer = 1
        ans = fit_piece(4, [4, 3, 5, 4, 6, 5, 7, 6, 6])
        assert (ans == real_answer)

        test = 6
        real_answer = 6
        ans = fit_piece(5, [1, 0, 1, 0, 1])
        assert (ans == real_answer)

        test = 7
        real_answer = 0
        ans = fit_piece(6, [1, 0, 1, 0, 1])
        assert (ans == real_answer)

        test = 8
        real_answer = 3
        ans = fit_piece(6, [0, 1, 1, 2, 0])
        assert (ans == real_answer)

        test = 9
        real_answer = 0
        ans = fit_piece(7, [1, 0, 1, 0, 1])
        assert (ans == 0)

        test = 10
        real_answer = 1
        ans = fit_piece(7, [0, 1, 1, 2, 0])
        assert (ans == 1)

    except AssertionError as msg:
        msg = "ASSERTION ERROR on test %d: \nYour Answer is %d but the correct answer is: %d" %(test, ans, real_answer)
        print(msg)

def tall_piece(top_row):
    fits = 0
    for i in range(len(top_row)):
        fits += 1 # Increment for the standing piece (x x x x)^T, where T is transponate.

        # Handle lying fit (x x x x) :
        if(i + 3 < len(top_row)):
            if(top_row[i] == top_row[i+1] == top_row[i+2] == top_row[i+3]):
                fits += 1

    return fits

def square_piece(top_row):
    fits = 0
    for i in range(len(top_row) - 1):
        # Just one rotation to care about:
        if(top_row[i] == top_row[i+1]):
            fits += 1

    return fits

def right_cannon_piece(top_row):
    fits = 0

    # Two rotations
    for i in range(len(top_row)):

        # Downwards rotation:
        if(i + 1 < len(top_row)):
            if(top_row[i] - 1 == top_row[i+1]):
                fits += 1

        # Cannon rotation:
        if(i + 2 < len(top_row)):
            if(top_row[i] == top_row[i+1] and top_row[i+1] + 1 == top_row[i+2]):
                fits += 1

    return fits

def left_cannon_piece(top_row):
    fits = 0
    for i in range(len(top_row)):
        # Downwards rotation:
        if(i + 1 < len(top_row)):
            if(top_row[i] == top_row[i+1] + -1):

                fits += 1

        # Cannon rotation:
        if(i + 2 < len(top_row)):
            if(top_row[i] - 1 == top_row[i+1] == top_row[i+2]):
                fits += 1

    return fits

def tri_piece(top_row):
    fits = 0
    for i in range(len(top_row)):
        # Rotation one the identity, T
        if(i + 2 < len(top_row)):
            if(top_row[i] - 1 == top_row[i+1] and top_row[i] == top_row[i+2]):
                fits += 1

        # 90 degree rotated T (counterclockwise)
        if(i + 1 < len(top_row)):
            if(top_row[i] - 1 == top_row[i+1]):
                fits += 1

        # 180 degree rotated T (Upside down aka horizontal flip)
        if(i + 2 < len(top_row)):
            if(top_row[i] == top_row[i+1] == top_row[i+2]):
                fits += 1

        # 90 degree rotated T (clockwise)
        if(i + 1 < len(top_row)):
            if(top_row[i] + 1 == top_row[i+1]):
                fits += 1

    return fits

def normal_l_piece(top_row):
    fits = 0
    for i in range(len(top_row)):
        # Identity Rotation L:
        if(i + 1 < len(top_row)):
            if(top_row[i] == top_row[i+1]):
                fits += 1
        # 90 degree rotated (counter clockwise)
        if(i+2 < len(top_row)):
            if(top_row[i] == top_row[i+1] == top_row[i+2]):
                fits += 1

        # 180 degree rotated:

        if(i+1 < len(top_row)):
            if(top_row[i] -2 == top_row[i+1]):
                fits += 1

        if(i+2 < len(top_row)):
            if(top_row[i] + 1 == top_row[i+1] == top_row[i+2]):
                fits += 1

    return fits

def right_l_piece(top_row):
    fits = 0
    for i in range(len(top_row)):
        # Identity rotation, vertically flipped L

        if(i + 1 < len(top_row)):
            if(top_row[i] == top_row[i+1]):
                fits += 1

        # 90 degree rotated counter clockwise:
        if(i+2 < len(top_row)):
            if(top_row[i] == top_row[i+1] == top_row[i+2]):
                fits += 1

        if(i + 1 < len(top_row)):
            if(top_row[i] +2 == top_row[i+1]):
                fits += 1

        if(i+2 < len(top_row)):
            if(top_row[i] == top_row[i+1] and top_row[i+2] + 1 == top_row[i]):
                fits += 1

    return fits

# Tries to fit a specific piece to the top row
def fit_piece(n, top_row):
    func_map = {1 : tall_piece,
                2 : square_piece,
                3 : right_cannon_piece,
                4 : left_cannon_piece,
                5 : tri_piece,
                6 : normal_l_piece,
                7 : right_l_piece}

    ans = int(func_map[n](top_row))
    return ans

# (KATTIS INPUT) List trick for inputs:
kattis = True
if(kattis):
    cols, piece = list(map(int, input().split()))
    top_row = list(map(int, input().split()))
    print(fit_piece(piece, top_row))
else:
    run_tests()
