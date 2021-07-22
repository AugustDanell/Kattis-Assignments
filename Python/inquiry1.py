numbers = int(input())
number_list = []
tot_sum = 0
for i in range(numbers):
    number = int(input())
    number_list.append(number)
    tot_sum += number

square_sum = 0
max = 0
for number in number_list:
    square_sum += number**2
    tot_sum -= number
    product = square_sum*tot_sum

    if(product > max):
        max = product

print(max)
