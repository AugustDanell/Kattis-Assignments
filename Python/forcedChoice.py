''' 
    General Solution Idea
    Forced Choice was a problem I had missed to do but it is very easy. Just take in cards in row 12 and disregard any deck, that is write remove, if that deck does not
    contain our secret prediction number P. Likeso, if it does, just print "KEEP" instead. 
'''

N, P, S = list(map(int, input().split()))
card_list = []
for i in range(1,N+1):
    card_list.append(i)

for i in range(S):
    cards = list(map(int, input().split()))[1:]
    if(P in cards):
        print("KEEP")
    else:
        print("REMOVE")
