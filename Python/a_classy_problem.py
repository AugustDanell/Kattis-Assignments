def class_to_num(s):
    switch = {
        "upper"  :  1.0,
        "middle" :  0.0,
        "lower"  : -1.0,
    }

    value = 0.
    class_split = s.split("-")
    tick_div = 1.

    for i in reversed(range(len(class_split))):
        #print("class split,", class_split[i])
        value += switch[class_split[i]] / tick_div
        tick_div *= 10.0

    return value

tests = int(input())
for i in range(tests):
    class_to_person_list_map = {}
    num_to_class_list_map = {}
    num_list = []

    people = int(input())
    for p in range(people):
        person, class_string, fluff = input().split()
        numeric_value = class_to_num(class_string)
        num_list.append(numeric_value)

        if(not class_to_person_list_map.__contains__(class_string)):
            class_to_person_list_map[class_string] = [person]
        else:
            class_to_person_list_map[class_string].append(person)

        if(not num_to_class_list_map.__contains__(numeric_value)):
            num_to_class_list_map[numeric_value] = [class_string]
        else:
            num_to_class_list_map[numeric_value].append(class_string)
    num_list.sort(reverse=True)

    printed_names = {}
    for n in num_list:
        class_list = num_to_class_list_map[n]
        name_list = []
        for c in class_list:
            current_class = class_to_person_list_map[c]
            name_list += current_class

        name_list.sort()
        for name in name_list:
            if(not printed_names.__contains__(name)):
                print (name[:-1])
                printed_names[name] = True

    print("="*30)
