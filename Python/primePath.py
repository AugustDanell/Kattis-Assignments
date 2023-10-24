# Problem Description: https://open.kattis.com/problems/primepath

import math
from collections import deque

# BFS algorithm to find minimum jumps:
def BFS(start, target, primes):
    
    # 1. Initiate supporting data structures:
    toVisit = deque([[start, 0]])
    visited = {}
    
    # 2. While the queue has packages, pop them and continue:
    while(len(toVisit) > 0):
        currentPackage = toVisit.popleft()
        currentNumber = currentPackage[0]
        currentTraversal = currentPackage[1]
        
        # 3. If the current package contains the target node, return:
        if currentNumber == target:
            return currentTraversal
            
        # 4. If not, and if we have not visited the current number, append new packages:
        elif currentNumber not in visited:
            visited[currentNumber] = True
            strNumber = str(currentNumber)
            
            # 5. For a number, append each new one-step transition, and increment traversals:
            for i in range(4):
                newStr = list(strNumber)
                for j in range(10):
                    if i == 0 and j == 0:
                        continue
                    else:
                        newStr[i] = chr(48+j)
                        nextNumber = int("".join(newStr))
                        if nextNumber in primes:
                            nextPackage = [nextNumber, currentTraversal+1]
                            toVisit.append(nextPackage)

# An algorithm used to quickly find out if the number N is prime:
def fastSieves(N):
    for i in range(2, int(math.sqrt(N))+1):
        if(N%i == 0):
            return False
    return True


if __name__ == "__main__":
    # 1. Initiate a map of primes, that we can use in the BFS later.
    primes = {}
    
    # 2. Use fastSieves to compute a constant map of every prime in the interval [2, 9999]:
    for candidate in range(2, 10000):
        if(fastSieves(candidate)):
            primes[candidate] = True
    
    # 3. Iterate over how many numbers to test:
    N = int(input())
    for _ in range(N):
        
        # 4. Print the lowest amount of steps from A -> B, using our map and the BFS function:
        a,b = list(map(int,input().split()))
        print(BFS(a,b, primes))
