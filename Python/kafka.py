
#Kafkaesque
signatures = int(input())
clerks = []
prev = 0
jumps = 0
for i in range(signatures):
    desknumber = int(input())
    if(desknumber<prev):
        jumps = jumps +1
    prev = desknumber




print(jumps+1)
