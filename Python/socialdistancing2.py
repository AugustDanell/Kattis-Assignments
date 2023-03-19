# Solution to the problem: https://open.kattis.com/problems/socialdistancing2

# 1. Read in data and initiate a dictionary / hashmap with every participant as non-seated (False):
S,N = list(map(int,input().split()))
seating = {}
for i in range(S):
    seating[i+1] = False

# 2. Read in the participants who are seated:
alreadySeated = list(map(int,input().split()))
for seat in alreadySeated:
    seating[seat] = True

# 3. Naively iterate looking at every seat and its next and previous seat:
new = 0
for currentSeat in range(1, S+1):
    
    # 4. If the current seat, the next seat and the previous seat are all non-taken, we take it now:
    prevSeat = currentSeat - 1
    if prevSeat == 0:
        prevSeat = S

    nextSeat = currentSeat +1
    if nextSeat == S + 1:
        nextSeat = 1
    
    if seating[prevSeat] == seating[currentSeat] == seating[nextSeat] == False:
        seating[currentSeat] = True
        
        # 5. In the event of taking the current seat, we also increment the counter:
        new += 1
        
# 6. Lastly we print the counter:
print(new)
