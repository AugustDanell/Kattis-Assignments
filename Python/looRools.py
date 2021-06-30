data = input()
split = data.split()

orglength = int(split[0])
length = orglength
usage = int(split[1])
startUsage = usage
roll = 1

while(not((length%usage == 0))):
    usage = usage - (length%usage)
    roll = roll +1
    #print(usage)
print(roll)