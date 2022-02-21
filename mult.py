mults = int(input())
start = True
candidates = []
start_cand = -14

for i in range(mults):
    c = int(input())
    if(start):
        start_cand = c
        start = False
    else:
        #print("C is", c, " and startcandidate is:", start_cand)
        if(c % start_cand == 0):
            start = True
            candidates.append(c)
            start_cand = c

for c in candidates:
    print(c)
