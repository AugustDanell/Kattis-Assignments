questions = int(input()) -1
a = input()
points = 0

for i in range(questions):
    b = input()
    if(b == a):
        points += 1

    a = b
print(points)
