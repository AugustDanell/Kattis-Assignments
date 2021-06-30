data = input()
split = data.split()

clauses = int(split[0])
variables = int(split[1])

if(clauses >= 8):
    print("satisfactory")

if(clauses < 8):
    print("unsatisfactory")
else:
    #Attempt to satisfy 3-sat
    clauseList = []
    guesses = ["1 2 3", "1 2 -3", "1 -2 3", "1 -2 -3",
               "-1 2 3", "-1 2 -3", "-1 -2 3", "-1 -2 -3"]

    for i in range(clauses):
        clauseList.append(input())

    satisfactory = False
    for i in range(8):
        guess = guesses[i]
        split = guess.split()
        x1 = split[0]
        x2 = split[1]
        x3 = split[2]
        isSat = True
        for j in range(clauses):
            clause = clauseList[j]
            split = clause.split()
            y1 = split[0]
            y2 = split[1]
            y3 = split[2]

            if((x1 == y1 or x2 == y2 or x3 == y3)):
               # print("Succesfull Match for clause:", (j+1))
               # print("Guess: ", guess)
               # print("Clause:", clause)
               # print("Go to clause:", str(j+2))
                None
            else:
                isSat = False
                #print("Unsuccesfull Match for guess", str(i+1), " and clause:", (j+1))
                #print("Guess: ", guess)
                #print("Clause:", clause)
                #print("Go to guess ", str(i+1))

        if(isSat):
            satisfactory = True
            break

    if(satisfactory):
        print("satisfactory")
    #else:
    #    print("unsatisfactory")