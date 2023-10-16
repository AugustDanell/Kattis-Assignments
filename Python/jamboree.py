# 780th Kattis: https://open.kattis.com/problems/jamboree
'''
    General Solution:
    A greedy algorithm that always takes the least uncombered scout,
    provided that said scout is not carrying two items.
'''

def findIndexLeastUncombered(l, twoItemScouts):
    leastUncomberedIndex = -1
    leastUncomberedWeight = float('inf')
    
    # 1. Iterate over every scout:
    for i in range(len(l)):
        
        # 2. If a scout is carrying two items, skip them
        if(i in twoItemedScouts):
            continue
        
        # 3. If a scout is carrying nothing, return them directly
        if l[i] == 0:
            return i
            
        # 4. If a scout is carrying less than the  lest uncombered, update:
        elif l[i] < leastUncomberedWeight:
            leastUncomberedIndex = i
            leastUncomberedWeight = l[i]
    
    # 5. Return the least uncombered
    return leastUncomberedIndex


if __name__ == "__main__":
    
    # 1. Read in data:
    N,M = list(map(int,input().split()))
    items = sorted(list(map(int, input().split())), reverse=True)
    scouts = [0]*M
    twoItemedScouts = {}
    
    # 2. Distribute items in a for-each loop:
    for item in items:
        
        # 3. Get the index of the least uncombered
        index = findIndexLeastUncombered(scouts, twoItemedScouts)
        
        # 4. Update the hash pertaining to two-items held:
        if(not scouts[index] == 0):
            twoItemedScouts[index] = True
            
        # 5. Give the item:
        scouts[index] += item
    
    # 6. Print the least uncombered scout:
    print(max(scouts))
