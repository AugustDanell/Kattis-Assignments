# Kattis ID: zebrasocelots
animals = int(input())
ocelotCount = 0
set = False

for i in range(animals):
    animal = input()
    #print(i)
    if(animal == "O"):
        ocelotCount += 2**(animals-(i+1))
        set = True

print(ocelotCount)
