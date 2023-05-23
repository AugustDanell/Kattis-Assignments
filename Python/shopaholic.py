# 682th Kattis. Greedy Solution to the problem: https://open.kattis.com/problems/shopaholic

N = int(input())
l = list(map(int,input().split()))
l = sorted(l, reverse=True)
discount = 0
for i in range(0+2, N, 3):
    discount += l[i]
print(discount)
