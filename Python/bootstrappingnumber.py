# 699th Kattis. A solution to the problem: https://open.kattis.com/problems/bootstrappingnumber

''' General Solution: Newton Raphsons method for finding a solution.
    We can rewrite the entire problem as an equation given the function f(x,n).
    We then calculate the derivative of f(x,n).
    We can then apply Newton Raphsons method for finding a solution.
    If we define a good starting guess and a reasonable tolerance to balance
    wrong answer / time limit exceeded, this solution is ok. 
'''


import math

def f(x,n):
    return x**x - n
def f_prime(x):
    return (x**x)*(math.log(x)+1)

n = int(input())
x = 9
tol = 1
while tol > 0.01:
    x_next = x - f(x,n)/f_prime(x)
    tol = abs(x**x - n)
    x = x_next

print(x)
