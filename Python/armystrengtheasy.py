# Solution to the problem: https://open.kattis.com/problems/armystrengtheasy

# Idea: All we need to do is compare the strongest monster of each army:
testcases = int(input())
for i in range(testcases):
    input()
    Ng,Nm = list(map(int,input().split()))
    Godzilla = list(map(int,input().split()))
    Mech = list(map(int,input().split()))

    Godzilla = sorted(Godzilla, reverse=True)
    mech = sorted(Mech, reverse=True)
    if(Godzilla[0] >= mech[0]):
        print("Godzilla")
    else:
        print("MechaGodzilla")
