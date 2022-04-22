def make_subtractions(dict, k, highest):
    while k > 0 and highest_counter > 0:
        #print(dict, k, highest)
        s = len(dict[highest])
        k -= s

        if(k >= 0):
            highest -= 1

    print(highest)

''' General Solution Idea
    1. Run the input. Let there be two hashmaps and a counter. The hashmap arr_occurances is an auxilary
    hashmap used to keep track of the occurances of a number. It maps a number to its occurance. This is
    used to keep track of a highest counter and also to construct a second hashmap, arr_counters. This
    second hashmap arr_counters will instead map the reverse, occurances to numbers that have reached
    that occurance.
    
    2. Handling the data. Here we are appending into the hashmaps accordingly.
    
    3. When we have the counter for the highest occurance, and the hashmap counting all the numbers
    that have reached that occurance, we can just subtract top down until we have our answer. This
    final step is done in the function make_subtractions().
'''

# 1.
n, k = list(map(int, input().split()))
arr_occurances = {}
arr_counters = {}
numbers = list(map(int, input().split()))
highest_counter = 0

# 2.
for i in range(n):
    number = numbers[i]

    # If a number exist increment it. Make changes to the counter map.
    if(arr_occurances.__contains__(number)):
        arr_occurances[number] = arr_occurances[number] + 1

        if(arr_counters.__contains__(arr_occurances[number])):
            arr_counters[arr_occurances[number]].append(number)
        else:
            arr_counters[arr_occurances[number]] = [number]

    # If a number does not exist add it. Make changes to the counter map.
    else:
        arr_occurances[number] = 1
        if(arr_counters.__contains__(1)):
            arr_counters[1].append(number)
        else:
            arr_counters[1] = [number]

    # Change the highest counter.
    if (arr_occurances[number] > highest_counter):
        highest_counter = arr_occurances[number]

# 3.
make_subtractions(arr_counters, k, highest_counter)
