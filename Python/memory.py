# My 735th Kattis, a solution to the problem: https://open.kattis.com/problems/memorymatch
''' General Solution:
    1. We are reading in the cards into a map that maps position -> card-value for every pick of 2 cards.
    2. If we find a pair we remove it immediately and we decrement n, the total number of cards. 
    3. If we find duplicates we remove them and we decrement n, the total number of cards, and we increment matches.
    
    4. CASE DIVISION:
    Every card so far that has not been a pair has been added into card_matching. We also have matches and n, describing 
    the matches that we have so far and the total of remaining cards with their backside upwards, respectively. 
    
    a) if n == 2, we can output the matches we have + 1 (because we can always find it).
    b) if len(card_mapping) >= n, we can also find the remaining cards and then we simply print: len(card_map)+matches
    c) else we just print the matches we have found thus far: print(matches)
'''

n = int(input())
m = int(input())
card_map = {}
for _ in range(m):
    c1,c2,v1,v2 = input().split()
    if not v1 == v2:
        card_map[c1] = v1
        card_map[c2] = v2
    else:
        n -= 2
        if c1 in card_map:
            card_map.pop(c1)
        if c2 in card_map:
            card_map.pop(c2)

matches = 0
rev_map = {}
pop_list = []
for key in card_map:
    val = card_map[key]
    if val in rev_map:
        matches += 1
        n -= 2
        pop_list.append(key)
        pop_list.append(rev_map[card_map[key]])
    else:
        rev_map[val] = key
for key in pop_list:
    card_map.pop(key)

if len(card_map) >= n//2:
    print(len(card_map) + matches)
elif n == 2:
    print(matches + 1)
else:
    print(matches)
