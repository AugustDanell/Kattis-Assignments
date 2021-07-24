trash, commands = list(map(int,input().split()))

people_map = {}
restart_sum = "0"

while(not commands == 0):
    command = input().split()
    if(command[0] == "SET"):
        people_map[command[1]] = command[2]
    elif(command[0] == "RESTART"):
        restart_sum = command[1]
        people_map = {}
    else:
        if(people_map.__contains__(command[1])):
            print(people_map[command[1]])
        else:
            print(restart_sum)

    commands -= 1
