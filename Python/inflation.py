N = int(input())
balloons = []
for i in range(1, N+1):
    balloon = N+1 - i
    balloons.append(balloon)

gasCanisters = list(map(int, input().split()))
gasCanisters.sort(reverse=True)
maxF = 0
minF = 1.5

# Match largest balloon with largest cannister:
for i in range(N):
    F = gasCanisters[i] / balloons[i]
    if F < minF:
        minF = F

    if F > 1.0:
        minF = 1.5
        break

if minF > 1.0:
    print("impossible")
else:
    print(minF)
