import math

data = input().split()
# Idea: We focus on the q-block and then try to fit
# 1-blocks into the same workload. If it can't be done
# we will have to extend the workload.

Q = int(data[0])
M = int(data[1])
S = int(data[2])
L = int(data[3])

Time = math.ceil(L/M)*Q

# TODO
# Now we need to work on the rest:
inv = math.ceil(L/M) - L/M
Rest = inv*M*Q
while(Rest < S):
    Time += 1
    Rest += M

print(Time)