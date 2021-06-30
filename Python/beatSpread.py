cases = int(input())
# Solution to Beat the Spread
for i in range(cases):
    data = input().split()
    sum = int(data[0])
    abs = int(data[1])
    found = False

    for j in range(0,1001):
        for k in range(0, j+1):
            #print(j,k)
            #print(j, k, j+k, j-k)
            #print(j-k)

            if((j+k) == sum and (j-k) == abs):
                found = True
                print(j,k)
                break

        if(found):
            break

    if(not found):
        print("impossible")