N, P, X, Y = list(map(int, input().split()))
meowpages = P // (N-1)
print(meowpages * Y + P * X)
