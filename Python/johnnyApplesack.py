# https://open.kattis.com/problems/applesack

''' General Solution:
    The solution to the problem is to use a
    greedy/brute force algorithm where we are 
    always moving back and forth to bring as 
    many apples as we can. We then go back to
    reclaim the apples, paying 1 apple for 
    every sack. 
'''

import math
if __name__ == "__main__":
    # 1. Read in base data:
    N,K = list(map(int,input().split()))
    d = 0

    # 2. For as long as we have apples, pay a sack:
    while(N > 0):
        passingToll = math.ceil(N/K)
        d += 1
        N -= passingToll

    # 3. Print the dist + 1, because we can travel up to the last toll booth.
    print(d+1)
