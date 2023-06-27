# 733th Kattis. A Solution to the problem: https://open.kattis.com/problems/kopabocker

# 1. Read in the data. 
N,M = list(map(int,input().split()))
postage_fees = {}
books_in_store = {}

# 2. Read into hashmaps the id and cost of every book in every store:
for i in range(M):
    books, fee = list(map(int,input().split()))
    postage_fees[i] = fee
    for _ in range(books):
        book_id, cost = list(map(int,input().split()))
        if i not in books_in_store:
            books_in_store[i] = [[book_id, cost]]
        else:
            books_in_store[i] += [[book_id, cost]]


# 3. Add a combinations variable such that we can iterate over a bit string indication an iteration over every combination of stores:
combinations = (2**M)

# 4. Iterate over every combination of a store, for example, 5 = 1001, means that we look in store 1 and store 4, we test this for 0000, to 1111, if M = 4:
best_cost = -1
for bin_sum in range(0, combinations):
    
    # 5. Add a map for taken books this iteration and make a binary string:
    taken_books = {}
    bin_str = bin(bin_sum)[2:]

    # 6. Add Padding to the binary string:
    while len(bin_str) < M:
        bin_str = "0" + bin_str

    # 7. For each time the binary string is 1 on index i, we use store i, that is to say we pay postage fee and we take its cheapest books:
    total_cost = 0
    for i in range(len(bin_str)):
        if bin_str[i] == "1":
            total_cost += postage_fees[i]
            books = books_in_store[i]
            for book in books:
                if book[0] in taken_books and book[1] < taken_books[book[0]] or book[0] not in taken_books:
                    taken_books[book[0]] = book[1]

    # 8. If we have all our books we calculate a total cost and if this cost is lower than the global total, we update the global total:
    if len(taken_books) == N:
        for key in taken_books:
            total_cost += taken_books[key]

        if best_cost == -1 or total_cost < best_cost:
            best_cost = total_cost

# 9. We print the global total: 
print(best_cost)
