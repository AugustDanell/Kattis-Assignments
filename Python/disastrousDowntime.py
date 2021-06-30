import math

inp = input()
split = inp.split()

requests = int(split[0])
maxRequests = int(split[1])

max = 1
requestList = []
servers = 1
runningRequest = int(input())
nextRequest = 0

for i in range(requests-1):
    request = int(input())
    if(servers == 1):
        nextRequest = request

    if(request - runningRequest >= 1000):
        runningRequest = nextRequest
        severs = servers - 1
        if(servers > max):
            max = servers
    else:
        servers = servers + 1

print(int(math.ceil(servers/maxRequests)))