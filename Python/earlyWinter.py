inp = input()
split = inp.split()

n = int(split[0])
dm = int(split[1])

inp = input()
split = inp.split()
winters = []
years = 0
foundSol = False

for i in range(n):
    year = int(split[i])
    if(year > dm):
        years = years +1
    else:
        foundSol = True
        break
    #winters.append(int(split[i]))

if(not(foundSol)):
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in %d years!" %(years))