S = input()
shots = int(len(S)/2)

Alice = 0
Barbara = 0

for i in range(shots):
    person = S[i*2]
    score = S[i*2 + 1]

    if(person == "A"):
        Alice += int(score)
    else:
        Barbara += int(score)

    if(Alice >= 11 and Alice-Barbara >=2):
        print("A")
        break
    if(Barbara >= 11 and Barbara-Alice >= 2):
        print("B")
        break
