def handle_single(single_data, digit_map):
    letter_by_letter = str(single_data)

    for i in letter_by_letter:
        digit = int(i)
        digit_map[digit] += 1

def handle_mult(data, digit_map):
    start = int(data[0])
    step  = int(data[2])
    end   = int(data[1])
    current = start
    steps = 0

    while current <= end:
        steps += 1
        handle_single(current, digit_map)
        current += step

    return steps

test_cases = int(input())
for i in range(test_cases):
    digit_map = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    street_name = input()
    print(street_name)
    adress_data = input()
    print(adress_data)
    adress_data = adress_data.split(" ")
    addresses = int(adress_data[0])

    visited_addresses = 0
    while visited_addresses < addresses:
        data = input().split()
        if(len(data) == 1):
            handle_single(data[0],digit_map)
            visited_addresses += 1
        else:
            visited_addresses += handle_mult(data[1:], digit_map)

    sum = 0
    for j in range(9+1):
        sum += digit_map[j]
        print("Make %d digit %d"%(digit_map[j],j))
    if(sum == 1):
        print("In total 1 digit")
    else:
        print("In total %d digits" %sum)
