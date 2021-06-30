import sys
def convertMinutes(m):
    return m*60

def convertHours(h):
    return 60*60*h

hour = 3600
s1 = 0
currentSpeed = 0
distance = 0.

for line in sys.stdin:
    data = line.split()
    subData = data[0].split(":")

    h2 = convertHours(int(subData[0]))
    m2 = convertMinutes(int(subData[1]))
    s2 = (int(subData[2]))

    s2 = s2 + h2 + m2
    time = s2-s1
    s1 = s2

    distance = distance + currentSpeed*time/hour
    if(len(data) > 1):
        currentSpeed = int(data[1])
    else:
        print("%s %5.2f km"%(data[0], distance))
        #print(data[0], distance, "km")