# 711th Kattis, A Solution To The Problem: https://open.kattis.com/problems/phonelist

'''
    General Solution: Nested Hashmaps for fast prefix finding.
    
    The problem is that we need to see if a number is the prefix of another number and this need to be done quickly.
    A solution is to have a long nest of hashmaps, where one hashmap correspond to one digit.
    Each time we iterate over a number we add the number as a hash, for example the number 912313 is added as:
    {9:{1:{2:{3:{1:{3:-1}}}}}}. The last insertion of "-1" is there to signify the end of the number.
    
    When we have this structure we can then iterate over each digit for a number to see if there is a prefixed number
    that we have previously come across. For example, if we have had 911, we will have a hashmap {9:{1:{1:-1}}}.
    When we later come across the number 9111231 we will iterate over each number and access the complete nest of hashmaps.
    We will see that we have a hashmap that maps 9 -> 1 -> 1 -> -1, meaning that we have come across a prefix.
'''

def prefix_checker(l):
    nestled_map = {}
    consistent = True
    for s in (l):

        # 1. Check for prefixes:
        if consistent:
            current_map = nestled_map
            for c in s:
                if c in current_map:
                    if current_map[c] == -1:
                        consistent = False
                        break
                    else:
                        current_map = current_map[c]
                else:
                    break

        # 2. Add numbers
        if consistent:
            current_map = nestled_map
            for i in range(len(s)):
                c = s[i]
                if i == len(s) - 1:
                    current_map[c] = -1
                elif c not in current_map:
                    current_map[c] = {}
                    current_map = current_map[c]
                else:
                    current_map = current_map[c]
    
    # 3. Output the answer:
    print(["NO", "YES"][int(consistent)])


# Driver Code:
for _ in range(int(input())):
    
    # 1. Read in the list:
    N = int(input())
    l = []
    for _ in range(N):
        l.append(input())
    
    # 2. Sort the entries based on length using a lambda function:
    sorting_func = lambda x: len(x)
    sorted_input = sorted(l, key = sorting_func)
    prefix_checker(sorted_input)
