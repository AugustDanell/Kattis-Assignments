# 734th Kattis and a solution to the problem: https://open.kattis.com/problems/alienmath

# 1. Read in input:
N = int(input())
digits = input().split()
digit_map = {}
for i in range(N):
    digit = digits[i]
    digit_map[digit] = i

# 2. Read through the input string:
s = list(input())
sub_str = ""
number = []
for c in s:
    sub_str += c
    if sub_str in digit_map:
        number.append(digit_map[sub_str])
        sub_str = ""

# 3. Calculate a digit sum:
digit_sum = 0
for i in range(len(number)):
    digit_sum += number[i] * (N)**(len(number) -1-i)

# 4. Print out the digit sum:
print(digit_sum)
