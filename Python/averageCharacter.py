# Solution Idea:
# Use "ord" to average the numerical ascii value over a text string and then use "chr" to convert it to the corrosponding ascii sign, flooring to fulfill
# the requirement that it should always take the smallest value if the ascii-numbers happen to fall within two integers. 

import math

text = input()
avg = 0

for c in text:
    avg += ord(c)

print(chr(math.floor(avg/len(text))))
