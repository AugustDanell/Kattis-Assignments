data = input().split()
N = int(data[0])
P = int(data[1])

problemData = input().split()
times = []
for i in range(N):
    times.append(int(problemData[i]))

if(times[P] > 300):
    print("0 0")
else:
    time = times[P]
    score = time
    times.pop(P)
    AC = 1
    times.sort()

    for t in times:
        time += t
        if(time > 300):
            break
        else:
            score += time
            AC += 1

    print(AC, score)