people = int(input())
line = input()
lineup = "1 "
number = 0

split = line.split()
for i in range (people-1):
    for j in range (people-1):
        if(int(split[j]) == number):
            lineup += (j+2).__str__() + " "
            number = number +1

print(lineup[:-1])