# Code Guessing
# Problem Simplification:
# 1. For each card between 1 to 9 there is a card with that digit on it.
# 2. A, B sees their own 2 cards.
# 3. A gives her cards to B.
# 4. B puts down the cards in increasing order.
# 5. Can A guess the uniquely put cards?


# Solution Idea:
# There are few possible cases (6 in total I think because it is (4! / 2! 2!) ):
# 1. ABBA: If A2 - A1 = 3, then she can guess. Else not.
# 2. AABB: Only if A2 = 7 can Alice guess correctly.
# 3. ABAB: Only if A1 = 6 and A2 = 8
# 4. BAAB: Only if A1 = 2 and A2 = 8
# 5. BABA: A2 = 1 and A2 = 3
# 6  BBAA: Possible if A1 = 3.

A1, A2 = list(map(int, input().split()))
constellation = input()

found = False
if(constellation == "ABBA"):
    if (A2 - A1) == 3:
        print(A1 + 1, A2 -1)
        found = True

elif(constellation == "AABB"):
    if(A2 == 7):
        print(8, 9)
        found = True

elif(constellation == "ABAB"):
    if(A1 == 6 and A2 == 8):
        print(7, 9)
        found = True

elif(constellation == "BAAB"):
    if(A1 == 2 and A2 == 8):
        print(1, 9)
        found = True

elif(constellation == "BABA"):
    if(A1 == 2 and A2 == 4):
        print(1,3)
        found = True

elif(constellation == "BBAA"):
    if(A1 == 3):
        print(1, 2)
        found = True

if(not found):
    print(-1)
