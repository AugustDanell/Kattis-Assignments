# Solution to the problem: https://open.kattis.com/problems/associativeexponents
a,b,c = list(map(int, input().split()))
if(a == 1 or (b == 2 and c == 2) or c == 1):
    print("What an excellent example!")
else:
    print("Oh look, a squirrel!")
