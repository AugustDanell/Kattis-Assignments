def check_duplicate(s):
    letter_map = {}
    duplicates = False
    for i in s:
        if(letter_map.__contains__(i)):
            duplicates = True
            break
        else:
            letter_map[i] = True

    return duplicates

name_list = []
names = int(input())
shortest_len = 1000

for i in range(names):
    name = input()
    if(len(name) >= 5):
        if(not check_duplicate(name)):
            name_list.append(name)
            if(shortest_len >= len(name)):
                shortest_len = len(name)

filtered_list = [x for x in name_list if len(x) == shortest_len]
filtered_list.sort()
if(len(filtered_list) > 0):
    print(filtered_list[-1])
else:
    print("neibb!")
