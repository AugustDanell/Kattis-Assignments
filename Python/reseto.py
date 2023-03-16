# Solution to the problem: https://open.kattis.com/problems/reseto

# A) Input and initialize:
N,K = list(map(int,input().split()))
crossedOutMap = {}
for number in range(2,(N+1)):
    crossedOutMap[number] = False
found = False
ans = -1
K-=1

# B) Iterate through every multiple, where every number is stored in the dictionary crossedOutMap:
for number in range(2, (N+1)):
    # 1. If it has already been crossed out, just skip over it in the loop:
    if crossedOutMap[number] == True:
        continue
    else:
        # 2. Else, cross out factors of the current number, if we find a factor, break and mark it as found:
        factor = 1
        while True:
            
            # 3. K == 0 means that if the current factor has not been crossed out, it is our target:
            if K == 0 and not crossedOutMap[number*factor]:
                break
            
            # 4. For as long as we have not found our target, keep crossing numbers out and decrement K: 
            if not crossedOutMap[number*factor]:
                K-=1
                crossedOutMap[number*factor] = True
            
            # 5. Have a built in check so as to avoid index out of bounds, else just increment factor:
            if number*(factor+1) > N:
                break
            else:
                factor += 1
        
        # 6. If we have K == 0 and the current number is not crossed out we set it as our answer and mark found as True:
        if K == 0 and not crossedOutMap[number*factor]:
            ans = number * factor
            found = True
    
    # 7. If the flag found is True there is no need to continue this loop:
    if found:
        break

# C) Print out the answer:
print(ans)
