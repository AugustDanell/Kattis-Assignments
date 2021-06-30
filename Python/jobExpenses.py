payments = int(input())
file = input()
split = file.split()
expenses = 0

for i in range(payments):
    payment = int(split[i])
    if(payment < 0):
        expenses += -payment

print(expenses)