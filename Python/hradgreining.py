line = input()
flag = False
for i in range(len(line) - 2):
    current = line[i]
    next = line[i+1]
    nextnext = line[i+2]
    if(current == "C" and next == "O" and nextnext == "V"):
        flag = True
        print("Veikur!")
        break

if(not flag):
    print("Ekki veikur!")