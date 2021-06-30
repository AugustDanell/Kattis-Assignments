while(1):
    info = input()
    if(info == "0 0"):
        break

    data = info.split()

    heads = int(data[0])
    tails = int(data[1])

    moves = 0
    if(tails == 0 and heads%2 == 1):
        print(-1)
    else:
        if(heads %2 == 0):
            while(not tails%4 == 0):
                tails += 1
                moves += 1

        else:
            # Heads %2 == 1
            while(not tails%4 == 2):
                tails += 1
                moves += 1

        heads += tails // 2
        moves += tails // 2
        tails = 0
        moves += heads // 2

        print(moves)