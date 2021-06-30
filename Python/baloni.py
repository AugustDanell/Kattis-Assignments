#Idea: We create a list of darts, called dartlist, which starts with
# the dart that pops the first balloon. For each subsequent balloon
# we look to the list and see if one of the darts in there pop the ballon.
# If so its height is decreased with one. A new dart is inserted if there
# are none.

# If still too slow:
# Consider the case of duplicates and of zeros.

balloons = int(input())
#balloonList = []
dartList = []
data = input().split()
for i in range(balloons):
    balloon = (int(data[i]))
    if(dartList.__contains__(balloon)):
        index = dartList.index(balloon)
        dartList[index] -= 1
    else:
        dartList.append(balloon-1)



print(len(dartList))