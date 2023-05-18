# My 670th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/missinggnomes
'''
    General Solution Idea:
    The idea is to iterate over each individual gnome. If the gnome exists (we use hashmap for constant
    average lookup time) we increase the count and try the next gnome. When we get our next gnome we 
    try to fit it in as early as possible with incrementing an index to fit it right in.
'''


N,M = list(map(int,input().split()))
gnomes = []
taken_gnomes = {}
for _ in range(M):
    gnome = int(input())
    gnomes.append(gnome)
    taken_gnomes[gnome] = True

index = 0
current_gnome = 1
while(current_gnome < N):
    if current_gnome not in taken_gnomes:
        if index < len(gnomes) and current_gnome > gnomes[index]:
            index +=1
        else:
            gnomes.insert(index, current_gnome)
            current_gnome += 1
            index += 1
    else:
        current_gnome += 1

if N not in taken_gnomes:
    gnomes.append(N)

for gnome in gnomes:
    print(gnome)
