tax = 0.3
shares = 0
avgCost = 0.

while(1):
    data = input().split()
    if(data[0] == "buy"):
        newShares = int(data[1])
        newCost = int(data[2])
        avgCost = ((avgCost*shares + newShares*newCost) /(shares+newShares))
        shares += newShares

        #print(avgCost)

    # sell case: The money is lost I think?
    if(data[0] == "sell"):
        shares -= int(data[1])


    if(data[0] == "split"):
        shares *= int(data[1])
        avgCost /= float(data[1])

    # Sold ones doesn't care
    if(data[0] == "merge"):
        #shares /= int(data[1])
        shares = int(shares / int(data[1]))
        avgCost *= float(data[1])


    #print(avgCost)
    #print(shares)
    if(data[0] == "die"):
        finalSell = float(data[1])
        profit = finalSell - avgCost
        if(profit > 0):
            print(shares*(finalSell - (profit*tax)))
        else:
            print(shares*finalSell)

        break

