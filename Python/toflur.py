# Assignment: https://open.kattis.com/problems/toflur

n = int(input())
l = list(map(int,input().split()))
l.sort()
score = 0

for i in range(1,n):
    score += (l[i] - l[i-1])**2
    
print(score)
