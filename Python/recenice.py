# 666th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/recenice

'''
    General Solution Idea:
    We have three functions for transforming a number into a string for said number, i.e, 16 = sixteen, etc.
    These functions use each other so 31 uses its own ten part and the one part for its last digit (from the one(n) function).
    This assignment is easy but also easy to make a mistake so we make use of asserts to test our solution as well as have
    a function called test() that we can check with a visual inspection.
'''

# Return a single digit number as a string. 0 is a special case, since it will not appear by itself. 
# For example: 110 = "onehundred" + "ten" + "".

def one(n):
    d = {0:"",
         1:"one",
         2:"two",
         3:"three",
         4:"four",
         5:"five",
         6:"six",
         7:"seven",
         8:"eight",
         9:"nine"}
    return d[n]

# Tens(n) deals with two digit numbers, making use of the one(n) function above for the last digit:
def tens(n):
    d = {10:"ten",
         11:"eleven",
         12:"twelve",
         13:"thirteen",
         14:"fourteen",
         15:"fifteen",
         16:"sixteen",
         17:"seventeen",
         18:"eighteen",
         19:"nineteen",
         20:"twenty",
         30:"thirty",
         40:"forty",
         50:"fifty",
         60:"sixty",
         70:"seventy",
         80:"eighty",
         90:"ninety"}

    if n in d:
        return d[n]
    else:
        ten_digit = d[(n//10)*10]
        one_digit = one(n%10)
        return ten_digit + one_digit

# hundred(n) makes use of the two earlier functions:
def hundred(n):
    hundred = one(n//100)
    ten = n%100
    ans = hundred + "hundred"
    if ten > 10:
        ans += tens(ten)
    elif ten > 0:
        ans += one(ten%10)

    return ans

assert tens(68) == "sixtyeight"
assert hundred(319) == "threehundrednineteen"
assert hundred(530) == "fivehundredthirty"
assert hundred(971) == "ninehundredseventyone"

# Take in any number and transform it ot the string version:
def num_to_str(num):
    if num >= 100:
        return hundred(num)
    elif num >= 10:
        return tens(num)
    else:
        return one(num)

# Run test function for visual inspection:
def test():
    for i in range(1,1000):
        print(num_to_str(i))

# Iterate over every number to find a suitable one, once it is found, insert it into l[index]:
def insert_count(word_count, l, index):
    count = 1
    
    # 1. Set the count to be one and then iterate until we find our counter, let number be a stringified version of count:
    while True:
        
        # 2. Depending on the value of count, use different functions to get the string:
        if(count >= 100):
            number = hundred(count)
        elif(count >= 10):
            number = tens(count)
        else:
            number = one(count)
        
        # 3. If a suitable count is found, insert it into the index and then return to exit the function:
        if count == (word_count + len(number)):
            l[index] = number
            return
        
        # 4. If not, just update the counter:
        count += 1

# 1. Readi n the data:
N = int(input())
l = []
index = -1
word_count = 0

# 2. Iterate over the word list:
for i in range(N):
    word = input()
    
    # 3. Once $ is found, update the index, else increment a word counter:
    if word == "$":
        index = i
    else:
        word_count += len(word)
    l.append(word)

# 4. Feed everything to insert count which will insert a string as a coutner on the right index, then we print everything using the join function:
insert_count(word_count, l, index)
print(" ".join(l))
