# 698th Kattis, A solution to the problem: https://open.kattis.com/problems/smallestcalculatedvalue
''' General Solution: Brute Force
    This is a brute force solution where we try every operations.
'''


from collections import deque
def op(operand1, operand2, operator):
    if(operator == "+"):
        return operand1 + operand2
    elif(operator == "-"):
        return operand1 - operand2
    elif(operator == "*"):
        return operand1*operand2
    elif(operator == "/" and operand1%operand2 == 0):
        return operand1//operand2

def left_to_right(l):
    A = op(l[0], l[2], l[1])

    if A == None:
        return None

    B = op(A, l[4], l[3])
    return B

min_val = -1
a,b,c = list(map(int,input().split()))
for op1 in ["+", "-", "*", "/"]:
    for op2 in ["+", "-", "*", "/"]:
        l = [a, op1, b, op2, c]
        val = left_to_right(l)
        if val == None or val < 0:
            continue
        if min_val == -1 or val < min_val:
            min_val = val

print(min_val)
