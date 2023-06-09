# A solution to the problem: https://open.kattis.com/problems/wizardofodds

N,K = list(map(int,input().split()))
print(["You will become a flying monkey!", "Your wish is granted!"][2**K >= N])
