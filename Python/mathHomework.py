b, d, c, l = list(map(int,input().split()))
combinations = []


for i in range(0, 250+1):
    if i*b > l:
        break

    for j in range(0, 250+1):
        if j*d > l:
            break

        for k in range(0, 250+1):
            if k*c > l:
                break

            if((i*b + j*d + k*c) == l):
                combinations.append([i, j, k])


if len(combinations) == 0:
    print("impossible")
else:
    for line in combinations:
        print(line[0], line[1], line[2])
