# 99 problems
# Input a number and if that number is less than 99 just output 99, there can be no other answer then.
# If the number is greater than 99, take the rest and either increment the compliment of that in Z99 if the number is greater than 49.
# If it is less, then just decrement the rest -1 (To offset Modulo)


number = int(input())
if number < 99:
    print(99)
else:
    rest = number % 100
    if(rest >= 49):
        print(number + (99-rest))
    else:
        print(number - rest - 1)
