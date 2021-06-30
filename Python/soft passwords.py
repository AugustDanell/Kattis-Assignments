def isDigit(d):
    if(d.isdigit()):
        return True
    else:
        return False

def caseReversal(S):
    T = ""
    for i in S:
        if(i.islower()):
            T = T + i.upper()
        elif(i.isupper()):
            T = T + i.lower()
        else:
            T = T + i
    return T


# Think about it as a complete n-graph
S = input()
P = input()

valid = False

# Identical
if(S == P):
    valid = True

# Digit in front or in back
if(len(P) + 1 == len(S)):
    if(isDigit(S[0])):
        if(S[1:] == P):
            valid = True
    if(isDigit(S[-1])):
        if(S[:-1] == P):
            valid = True

P = caseReversal(P)

# Case Reversal
if(P == S):
    valid = True

if(valid):
    print("Yes")
else:
    print("No")