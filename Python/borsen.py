# A solution to the problem: https://open.kattis.com/problems/borsen

'''
General Idea:
The general idea for this kind of problem can be to always buy/sell a stock and then have a function to undo that. For example we have 100 dollars. We see a stock worth
70 dollars, we buy all we can. The next stock is a stock worth 60 dollars. It would have been globally better to buy the 60 dollar stock, so we undo the purchase of the
70 dollar. We can do this by saving the money we had before purchase as well as the stocks we hade before selling.
'''

def buy_stock(money,stock,fee):
    return (money-fee)/stock
def sell_stock(stocks, money_per_stock, fee):
    return money_per_stock*stocks - fee

if __name__ == "__main__":
    
    # 1. Read in input:
    n = int(input())
    fee = float(input())
    money = 100
    stocks = 0
    stock_price = 0

    # 2. Iterate over stocks. Sell and buy greedily. If it is a bad decision, we redact it upon the next iteration:
    for _ in range(n):
        stock = float(input())
        if stock_price == 0 or stock < stock_price:
            current_stocks = buy_stock(money, stock, fee)
            if current_stocks > stocks:
                stock_price = stock
                stocks = current_stocks

        elif stock > stock_price:
            current_money = sell_stock(stocks, stock, fee)
            if current_money > money:
                money = current_money
                stock_price = stock
    print(money)
