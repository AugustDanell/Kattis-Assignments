# A solution to the problem: https://open.kattis.com/problems/parket

outer, inner = list(map(int,input().split()))
blocks = outer + inner
ans = []

# 1. Linearly try every subdivision:
for x in range(1, blocks):
    
    # 2. The two factors f1 = x and f2 = inner/x need to be integers, if not we discard it:
    if not inner % x == 0:
        continue
    
    # 3. Let the two sums f1 and f2 be defined as below:
    f1 = x
    f2 = inner//x

    # 4. Define a check for the two factors, to see if f1 and f2 can be contained by the total amount of blocks:
    check = (f1+2)*(f2+2)
    if check == blocks:
        ans=[f1 +2, f2+2]
        break

# 5. Output the answers:
print("{0} {1}".format(max(ans), min(ans)))
