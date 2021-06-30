s1 = input()
split1 = s1.split()

leave = int(split1[0])
classStart = int(split1[1])
transits = int(split1[2])
time = classStart - leave

s2 = input()
split2 = s2.split()

walks = []
rides = []
arrivals = []

for i in range(transits+1):
    walks.append(int(split2[i]))

s3 = input()
split3 = s3.split()

for i in range(transits):
    rides.append(int(split3[i]))


s4 = input()
split4 = s4.split()

for i in range(transits):
    arrivals.append(int(split4[i]))

accumulatedTime = 0
for i in range(transits):
    accumulatedTime = accumulatedTime + walks[i]
    accumulatedTime = accumulatedTime + rides[i]
    waitTime = accumulatedTime%arrivals[i]
    accumulatedTime = accumulatedTime + waitTime

accumulatedTime = accumulatedTime + walks[transits]

if(accumulatedTime > time):
    print("no")
else:
    print("yes")