friends = int(input())
Birthday_Map = {}
name_list = []

for i in range(friends):
    name, like, date = input().split()
    like = int(like)

    if(not Birthday_Map.__contains__(date)):
        Birthday_Map[date] = [name, like]
        name_list.append(name)
    else:
        internal_like = Birthday_Map[date][1]
        internal_name = Birthday_Map[date][0]

        if(like > internal_like):
            Birthday_Map[date] = [name, like]
            name_list.remove(internal_name)
            name_list.append(name)

name_list.sort()
print(len(name_list))
for i in name_list:
    print(i)
