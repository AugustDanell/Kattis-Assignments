'''
Solution Idea:
I did this problem in C and only got a partial solution before, due to poor time complexity. However, the problem can be optimized similar to the Sieves algorithm for factorizing primes.
Naive_Sieves(N) is an algorithm that checks divisability from 1..N, but this can be optimized, because if we have not found a divisor from 1..sqrt(N), then there can be no divisor after that range.
Why? Because we would have found it already. If N = f_1 * f_2, the worst case for a non-prime would happen when f1=f2=sqrt(N). This would cause the largest amount of iterations we need to do. 
We can extrapolate the same concept from naive_sieves and sqrt_sieves to the multiplication table. If we have a factor larger than the square root of M we can break prematurely because we have already
found f_1*f_2 once before, so we can just increment Q with 2 to account for this. The exception to this rule is when M = f_1*f_2, and f_1 = f_2. For example, M = 9, N = 5. Factor = 3 need to be accounted 
only once. 
'''


import math

# 1. Read in the data:
N,M = list(map(int,input().split()))
Q = 0

# 2. Iterate over every factor:
for factor in range(1, N+1):
  
    # 3. If we are outside sqrt(M) then we break prematurely, no reason to continue:
    if factor > math.sqrt(M):
        break
    else:
        # 4. Else we check divisibility:
        if M%factor == 0 and M//factor <= N:
          
            # 5. Lastly we also check for the exception of double factors, that is to say, f_1 = f_2, where M = f_1*f_2:
            if factor == M//factor:
                Q += 1
            else:
                Q += 2

# 6. Print the result:
print(Q)
