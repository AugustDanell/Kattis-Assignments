# Solution to the problem: https://open.kattis.com/problems/redistribution

# 1. Take in input:
totalRooms = int(input())
roomExams = list(map(int,input().split()))
roomMap = {}
roomList = []
totalExams = 0

# 2. Read in rooms 1 .. N, and append the room into a map as well as their corrosponding value (how many exams they hold).
for room in range(1, totalRooms + 1):
    roomMap[room] = roomExams[room-1]
    roomList.append(room)
    totalExams += roomExams[room-1]

# 3. Create a lambda function to sort on exams in the room, based on the map:
sortOnExams = lambda x: roomMap[x]
sortedRooms = sorted(roomList, key=sortOnExams, reverse=True)

# 4. Assume that invalid is false and run a check for each room. If a room has more exams than the total - that room, set invalid to true.
invalid = False
for exams in roomExams:
    if exams > totalExams - exams:
        invalid = True

# 5. Print the answer based on the invalid flag:
if not invalid:
    print(" ".join(list(map(str,sortedRooms))))
else:
    print("impossible")

