# A solution to the problem: https://open.kattis.com/problems/han

def chr_to_num(c):
    return ord(c)-97
def num_to_chr(n):
    return chr((n%26)+97)

def add_laps(chr_map, laps):
    for key in chr_map.keys():
        chr_map[key] += laps

def add_new_steps(chr_map, start, steps, reverse):
    current = start
    while steps > 0:
        steps -= 1
        chr_map[chr(97 + current % 26)] += 1
        if not reverse:
            current += 1
        else:
            current -= 1

# 1. input:
queries = int(input())
reverse = False
chr_mapping = {}
current_pos = 0
current_n = 0

# 2. Init:
for i in range(0, 26):
    chr_mapping[chr(97+i)] = 0

# 3. Iterate over the queries:
for _ in range(queries):

    # 4. Read the query, the next position and the amount of steps to get there:
    query = input().split()
    next_pos = int(query[1])
    steps = int(query[1]) - current_n

    if(query[0] == "SMJER"):
        steps -= 1

    # 5. Append every value we can provided that we can make a lap:
    laps = steps // 26
    if laps > 0:
        add_laps(chr_mapping, laps)

    # 6. Append new values according to our steps:
    add_new_steps(chr_mapping, current_pos, steps%26, reverse)

    # 7. Adjust the pointer according to reversal:
    if not reverse:
        current_pos += steps
    else:
        current_pos -= steps
    
    # 8. Read in operation. If Upit, remember to print:
    if(query[0] == "UPIT"):
        queried_chr = query[2]
        print(chr_mapping[queried_chr])
    else:
      # 9. If the operation is SMJER, decrement pointer position but before doing so, increment its value:
        chr_mapping[num_to_chr(current_pos)] += 1
        if not reverse:
            current_pos -= 1
        else:
            current_pos += 1
      
      # 10. Set reverse to be its non-boolean value:
        reverse = not reverse


    current_n = next_pos
    #print(query[0], query[1], reverse, current_pos%26, chr_mapping)
