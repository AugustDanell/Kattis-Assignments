# Solution to the problem: https://open.kattis.com/problems/eveningout1
A,B = list(map(int,input().split()))
print(min(A%B, B-(A%B)))
