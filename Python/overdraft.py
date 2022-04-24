# Solution Idea: 
# Just iterate through each transaction. If a transaction leaves you with less than 0, just increment up to the point that will not leave you missing money. 

transactions = int(input())
money_sum = 0
start_sum = 0

for i in range (transactions):
    money_sum += int(input())

    if(money_sum < 0):
        start_sum += -(money_sum)
        money_sum = 0

print(start_sum)
