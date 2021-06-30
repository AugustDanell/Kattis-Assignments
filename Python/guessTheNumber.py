import sys

lower = 1
upper = 1000
isCorrect = False

while(not isCorrect):
    ans = int((lower + upper)/2)
    print(ans)
    out = input()

    if(out == "correct"):
        isCorrect = True
    elif(out == "higher"):
        lower = ans + 1
    else:
        upper = ans - 1

    sys.stdout.flush()