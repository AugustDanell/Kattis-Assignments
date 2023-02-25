saidAnimal = input()
animals = int(input())
attackAnimals = []
counterAnimals = {}

for i in range(animals):
    animal = input()
    if animal[0] == saidAnimal[-1]:
        attackAnimals.append(animal)

    if counterAnimals.__contains__(animal[0]):
        counterAnimals[animal[0]] += 1
    else:
        counterAnimals[animal[0]] = 1

# First animal not guaranteeing an elimination:
anyAnimal = ""
if len(attackAnimals) > 0:
    anyAnimal = attackAnimals[0]

# Try to find an eliminationAnimal
elminationAnimal = ""
for animal in attackAnimals:
    if not counterAnimals.__contains__(animal[-1]) or (counterAnimals[animal[-1]] == 1 and animal[0] == animal[-1]):
        elminationAnimal = animal
        break

# OUTPUT to Kattis:
if(not elminationAnimal == ""):
    print("{0}!".format(elminationAnimal))
elif(not anyAnimal == ""):
    print(anyAnimal)
else:
    print("?")
