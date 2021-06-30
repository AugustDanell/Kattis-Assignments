cases = int(input())
for i in range(cases):
    data = input().split()
    gnomes = int(data[0])
    for j in range(1, gnomes):
        x = int(data[j])
        y = int(data[j+1])

        if(not y - x == 1):
            print(j+1)
            break
