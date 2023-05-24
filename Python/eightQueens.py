# 685th Kattis. A solution to the problem: https://open.kattis.com/problems/8queens

''' General Solution:
    Iterate over two tuples (r1,c1) and (r2, c2). Check that: 
    
    1. (r1 =//= r2 and c1 =//= c2)
    2. (r1,c1) == Queen and (r2, c2) == Queen
    3. Queen(r1,c1) threatens Queen(r2, c2).
    
    If all of these requirements are met, set the flag to invalid. As for "threatens"
    we can check:
    
    1. r1 and r2 are the same.
    2. or, c1 and c2 are the same
    3. or, (r1,c1) and (r2, c2) are on a diagonal. To check this we let a constant 
    go from 0-7 which we can use for both addition and subtraction of thw two operands.
    A total of 2**2 = 4 operations where we check if the added diagonal threatens the other queen:
    
    1. (r1+d, c1+d) == (r2, c2)
    2. (r1+d, c1-d) == (r2, c2)
    3. (r1-d, c1+d) == (r2, c2)
    4. (r1-d, c1-d) == (r2, c2)
'''

chessboard = []
queens = 0
for _ in range(8):
    row = list(input())
    queens += row.count("*")
    chessboard.append(row)

invalid = not(queens == 8)
for r1 in range(8):
    for c1 in range(8):
        for r2 in range(8):
            for c2 in range(8):
                if ((r1 == r2 and c1 == c2) or (chessboard[r1][c1] == "." or chessboard[r2][c2] == ".")):
                    continue

                if (r1 == r2 or c1 == c2):
                    invalid = True

                for dia_constant in range (1,8):
                    if r1 + dia_constant == r2 and c1 + dia_constant == c2:
                        invalid = True

                    if r1 + dia_constant == r2 and c1 - dia_constant == c2:
                        invalid = True

                    if r1 - dia_constant == r2 and c1 + dia_constant == c2:
                        invalid = True

                    if r1 - dia_constant == r2 and c1 - dia_constant == c2:
                        invalid = True



if (invalid):
    print("invalid")
else:
    print("valid")
