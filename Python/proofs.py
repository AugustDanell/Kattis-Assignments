lines = int(input())
assumption_map = {}
err_line = -1
err = False

for i in range(lines):
    line = input().split()
    j = 0
    while(not line[j] == "->"):
        if(not assumption_map.__contains__(line[j])):
            err_line = i+1
            err = True
            break
        j+=1

    if(err):
        break
    else:
        j+= 1
        for k in range(j,len(line),1):
            assumption_map[line[k]] = True

if(err):
    print(err_line)
else:
    print("correct")
