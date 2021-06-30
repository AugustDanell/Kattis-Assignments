data = input().split()
houses = int(data[0])
watches = int(data[1])
prev = 0
safe = 0

for i in range(watches):
    inp = int(input())
    safeRuns = (inp - prev)*(houses-(inp-1))
    #print(inp, safeRuns)
    safe += safeRuns
    prev = inp

print(safe)