commands = int(input())
volume = 7
for i in range(commands):
    command = input()
    if(command == "Skru op!" and volume < 10):
        volume += 1
    elif (command == "Skru ned!" and volume > 0):
        volume -= 1

print(volume)
