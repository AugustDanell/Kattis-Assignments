# A solution to the problem: https://open.kattis.com/problems/akcija

N = int(input())
remaining_books = []
for _ in range(N):
    book = int(input())
    remaining_books.append(book)

remaining_books = sorted(remaining_books, reverse=True)
total = sum(remaining_books)

for i in range(2,N,3):
    total -= remaining_books[i]

print(total)
