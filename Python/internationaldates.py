# Quick solution to: https://open.kattis.com/problems/internationaldates

date = list(map(int,input().split("/")))
if(int(date[0]) > 12):
    print("EU")
elif(int(date[1]) > 12):
    print("US")
else:
    print("either")
