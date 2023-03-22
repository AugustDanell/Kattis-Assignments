# A complete solution to the problem: https://open.kattis.com/problems/busskortet

# 1. Take in input. Initiate a sum s, which we call total sum and a counter:
s = int(input())
transactions = 0

# 2. Always reduce s down to below 500, count transactions as we do:
while s > 500:
    transactions += 1
    s -= 500

# 3. If the new sum is within: s in [401, 500], ans = transactions + 1 (because we just append a last 500 transaction):
if s >= 401:
    print(transactions + 1)
else:
    # 4. If s is in [0, 400], we reduce again to [0, 199], incrementing the counter as we go:
    while s >= 200:
        transactions += 1
        s -= 200

    # 5. Since we have reduced s with a multiple of 200 we can be in the range [0, 199]. If we happen to be done print that:
    if s == 0:
        print(transactions)
    else:
        # 6. Else, we can append one last 200 if s > 101, else one last 100. Either way this will surmount to one last transaction:
        print(transactions+1)
