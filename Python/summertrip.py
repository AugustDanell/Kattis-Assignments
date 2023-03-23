# A solution to the problem: https://open.kattis.com/problems/summertrip

# 1. Take in an input string and initiate a total counter:
s = input()
total = 0

# 2. Iterate through every letter with the index i and define a current = s[i]:
for i in range(len(s)):
    current = s[i]
    nextIndex = i+1
    counter = 0
    uniques = {}

    # 3. Define a next index which is an index from i+1 to n. Let next = s[nextIndex]:
    while nextIndex < len(s):
        next = s[nextIndex]
        
        # 4. Break the loop if the criteria that the first element in the substring, which we call current, is not unique:
        if next == current:
            break
        
        # 5. Else, we check if the last is unique. If it is not we can still increment nextIndex to search for new matches:
        elif not uniques.__contains__(next):
            counter += 1
        
        # 6. Do just that, and mark next as visited for future iterations:
        nextIndex += 1
        uniques[next] = True
    
    # 7. Sum up the total amount of matches:
    total += counter

# 8. Print out the total amount of matches
print(total)
