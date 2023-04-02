# A solution to the trivial problem: https://open.kattis.com/problems/addingtrouble

l=list(map(int,input().split()))
if(l[0] + l[1] == l[2]):
    print("correct!")
else:
    print("wrong!")
