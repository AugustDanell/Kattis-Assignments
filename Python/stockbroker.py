# 689th Kattis. A solution to the problem: https://open.kattis.com/problems/stockbroker

''' General Solution: Greedy Algorithm
    This problem is one such problem where we can buy and sell stocks and we should calculate the max sum of profit.
    We can iterate over each stock and we opt to buy every stock where we see that the next stock is of a higher price.
    Similarily we opt to sell every stock where the next stock is of a lower price. This is a greedy algorithm but it works.
    We have to make sure that we update the stocks properly and that we follow the rule that says that we cannot own anymore
    than 1e5 stocks at any time. 
'''

N = int(input())
money = 100
stocks = 0.0

stock_prices = []
for _ in range(N):
    stock_prices.append(int(input()))

for i in range(len(stock_prices)-1):
    if money > 0:
        current = stock_prices[i]
        next_stock = stock_prices[i+1]
        if next_stock > current:
            new_stocks = min(money // current, 10**5 - stocks)
            money = money - (new_stocks*current)
            stocks += new_stocks

    if stocks > 0:
        current = stock_prices[i]
        next_stock = stock_prices[i+1]
        if next_stock <= current:
            money += stocks * current
            stocks = 0

print(int(money + stocks*stock_prices[-1]))
