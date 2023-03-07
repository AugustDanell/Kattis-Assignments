# Assignment: https://open.kattis.com/problems/babypanda

day, totalSlimes = list(map(int,input().split()))
l = list("{0:b}".format(totalSlimes))
print(l.count("1"))
