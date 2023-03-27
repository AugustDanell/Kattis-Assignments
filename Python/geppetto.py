# A solution to the problem: https://open.kattis.com/problems/geppetto

def choices(n, binaryChoices):
    N = 2**n

    # 1. If we have c choices start with n = 2**c and then we try to trim away bad strings:
    total = N

    # 2 Iterate from 2 to n (exclusive) to create possible bit strings via the bin() func.
    for b in range(2, N):
        bin_str = bin(b)[2:]

        # 3. For every binary string we see if a pair has indices of matching 1's for disqualification:
        for pair in binaryChoices:
            i1,i2 = (pair[0]-1), (pair[1]-1)

            # 4. I got stuck before this step. I 
            while len(bin_str) < n:
                bin_str = "0" + bin_str

            # 5. See if the current pair disqualifies this string:
            if bin_str[i1] == "1" and bin_str[i2] == "1":
                total -= 1
                break

    # 6. Return the potentially trimmed total number:
    return total

# 1. Input:
N,M = list(map(int,input().split()))
pairs = []
pair_strings = {}

# 2. Read in pairs and use a hashmap to see that the pair is unique:
for i in range(M):
    pair = input().split()
    if pair_strings.__contains__(pair[0]) and pair_strings[pair[0]].__contains__(pair[1]):
        continue
    elif pair_strings.__contains__(pair[1]) and pair_strings[pair[1]].__contains__(pair[0]):
        continue

    if pair_strings.__contains__(pair[0]):
        pair_strings[pair[0]][pair[1]] = True
    else:
        pair_strings[pair[0]] = {pair[1]:True}
    
    # 3. Append the pair so it will not be added again (nor its inverse).
    pairs.append(list(map(int,pair)))

# 4. Call the function choices which will return how many choices there are as an answer: 
print(choices(N,pairs))
