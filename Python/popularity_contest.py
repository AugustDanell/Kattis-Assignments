N,M = list(map(int,input().split()))
success = 1
success_factors = []
friend_factors = []

# Init the success factor:
for s in range(N):
    success_factors.append(success)
    success += 1

# Init as no friends:
for i in range(N):
    friend_factors.append(0)

# Append friendships:
for f in range(M):
    f1, f2 = list(map(int,input().split()))
    friend_factors[f1-1] += 1
    friend_factors[f2-1] += 1

# Append coefficients (slow):
coeff = []
for c in range(N):
    coeff.append((friend_factors[c] - success_factors[c]).__str__())

print(' '.join(coeff))
