if __name__ == "__main__":
    symbolToCost = {".":20,
                    "O":10,
                    "\\":25,
                    "/" : 25,
                    "A" : 35,
                    "^" : 5,
                    "v" : 22}

    N,M = list(map(int,input().split()))
    cost = 0
    for _ in range(N):
        for symbol in list(input()):
            cost += symbolToCost[symbol]

    print(cost)