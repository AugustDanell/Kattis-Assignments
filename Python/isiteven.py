# 684th Kattis. A solution to the problem: https://open.kattis.com/problems/isiteven

N,K = list(map(int,input().split()))
two_count = 0
for _ in range(N):
    number = int(input())
    if two_count <= K:
        while number % 2 == 0:
            number //= 2
            two_count += 1
            if two_count == K:
                break

print(int(two_count >= K))
