# 674th Kattis Solution. Solution to the problem: https://open.kattis.com/problems/simplearithmetic 
# General solution: Basically just using the decimal package for 

import decimal
d1, d2, d3 = list(map(int, input().split()))
a = decimal.Decimal(d1)
b = decimal.Decimal(d2)
c = decimal.Decimal(d3)
print(a*b/c)
