# 692th Kattis. A solution to the problem: 
''' General Solution: Regex
    Just match a regex with numbers and find the largest number.
    There are easy solutions but I wanted to relearn some regex.
''' 

import re
chrs = int(input())
txt = input()
numbers = re.findall("[0-9]+", txt)
largest = -1
for number in numbers:
    if int(number) > largest:
        largest = int(number)

print(largest)
