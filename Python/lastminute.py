Aunique, Bunique, Arest, Brest = list(map(int,input().split()))
if Arest == 0 and Brest == 0:
    print(min(Aunique, Bunique))

elif(Arest == 0):
    print(Aunique)

elif(Brest == 0):
    print(Bunique)

else:
    print(Aunique + Bunique + Arest * Brest)
