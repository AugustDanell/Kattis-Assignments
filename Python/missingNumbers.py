numbers = int(input())
start = int(input())
nlist = [start]
correct = True

for i in range(numbers-1):
    nlist.append(int(input()))

for j in range(nlist[-1]):
    number = 1 + j
    if(not (number in nlist)):
        print(number)
        correct = False

if((correct)):
   print("good job")