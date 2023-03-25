# A solution to the problem: https://open.kattis.com/problems/rotatecut

# 1. Iterate over amount of testcases T:
testcases = int(input())
for T in range(testcases):
    # 2. For each testcase T, read in the original text and amount of cuts:
    cuts, text = input().split()
    cuts = int(cuts)
    
    # 3. For every cut, break if our current length is less than 4. Else continue to cut and rotate.
    for cut in range(1, cuts+1):
        if len(text) < 4:
            break
        
        # 4. The cut length should be the length of the remaining text, floor-divisioned by 4:
        cutLength = len(text)//4
        
        # 5. If cut is congruent with 1, just cut it. Else rotate it, cut it, and rotate it back (lazy style):
        if cut % 2 == 1:
            text = text[cutLength:]
        else:
            text = text[::-1]
            text = text[cutLength:]
            text = text[::-1]
        #print(text)
    
    # 6. Print the non-rotated version of the text as per the description:
    print(text)
