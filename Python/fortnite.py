#Solution to Epig Dance off
inp = input()
data = inp.split()

rows = int(data[0])
cols = int(data[1])

video = []
moves = 0
for i in range(rows):
    video.append(input())

prevCoordinates = []
coordinates = []
for i in range (cols):
    increase = True
    for j in range (rows):
        marker = (video[j])[i]
        if(marker == "$"):
            coordinates.append(i)
            for val in ([i-1,i,i+1]):
                if val in prevCoordinates:
                    increase = False
                    break
        if(not(increase)):
            break

    if(increase and not(i == 0)):
        moves = moves + 1

    prevCoordinates = coordinates

print(moves + 1)