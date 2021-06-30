offers = ""
while(1):
    offers = input()

    if(offers == "0 0"):
        break

    data = offers.split()
    n = int(data[0])
    m = int(data[1])

    found = False
    bestPrice = 100.
    bestVal = 100.
    bestTickets = 0

    for i in range(n):

        ticketData = input().split()
        tickets = int(ticketData[0])
        price = int(ticketData[1])
        val = price / tickets
        if(tickets > m):
            continue

        found = True
        if(val < bestVal):
            bestTickets= tickets
            bestVal = val
            bestPrice = price

        elif(val == bestVal):
            if(tickets > bestTickets):
                bestTickets = tickets
                bestVal = val
                bestPrice = price

    if(not found):
        print("No suitable tickets offered")
    else:
        print("Buy %d tickets for $%d" %(bestTickets, bestPrice))
