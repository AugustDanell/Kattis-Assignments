data = input().split()
systems = int(data[0])
ships = int(data[1])

finnisMovements = []
shipData = input().split()
for i in range(systems):
    finnisMovements.append(int(shipData[i]))

finnisMovements.sort()

won = 0
for i in range(systems):
    if(ships > finnisMovements[i]):
        ships -= finnisMovements[i] + 1
        won += 1
    else:
        break

print(won)