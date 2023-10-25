# Problem Description: https://open.kattis.com/problems/checkingforcorrectness

import sys
def fasterExponentation(A,B,M):
    # 1. Initiate data:
    result = 1
    A %= M

    # 2. While we have exponents to play with, square A relative mod M and if B is odd, append A to the result:
    while B > 0:
        if B % 2 == 1:
            result = (result * A) % M

        A = (A*A)%M
        B //= 2

    # 3. Return the result:
    return int(result)

# Driver code:
if __name__ == "__main__":

    # 1. Read in every line until EOF signal is given:
    for line in sys.stdin:

        # 2. From "line", parse data:
        a, op, b = line.split()
        a = int(a)
        b = int(b)
        m = 10000

        # 3. Check different operations and print the result accordingly
        if(op == "+"):
            print(int((a+b)%m))
        elif(op == "*"):
            print(int((a*b)%m))
        else:
            print(fasterExponentation(a,b,m))
