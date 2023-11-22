if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    data = list(map(int, input().split()))
    fishes = sorted(data)
    peopleList = []
    for _ in range(m):
        quantity, price = list(map(int,input().split()))
        peopleList.append([quantity, price])
    sortedPeople = sorted(peopleList, key = lambda x: x[1])

    totalPrice = 0
    while len(sortedPeople) > 0 and len(fishes) > 0:
        bestPerson = sortedPeople.pop()
        quantity, price = bestPerson
        bestFish = fishes.pop()
        totalPrice += price*bestFish
        quantity -= 1
        if quantity > 0:
            sortedPeople.append([quantity, price])
       # print(totalPrice, sortedPeople, fishes)

    print(totalPrice)
