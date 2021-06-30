cases = int(input())
for i in range(cases):
    disks = int(input())
    data = input().split()
    count = 0
    order = 1

    for j in range(disks):
        if(int(data[j]) == order):
            order += 1
        else:
            count += 1

    print(count)