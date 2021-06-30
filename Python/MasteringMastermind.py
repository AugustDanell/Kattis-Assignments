guess = input()

# Check identical position and color:
I = 0
data = guess.split()
letters = int(data[0])

E = data[1]
D = data[2]
Emap = {}
Dmap = {}
for i in range(letters):
    if(E[i] == D[i]):
        I += 1
    else:
        if(not Emap.__contains__(E[i])):
            Emap[E[i]] = 1
        else:
           Emap[E[i]] = Emap[E[i]] + 1


        if(not Dmap.__contains__(D[i])):
            Dmap[D[i]] = 1
        else:
            Dmap[D[i]] = Dmap[D[i]] + 1


l = list(Emap)
s = 0
#print(l)
for e in Emap:
    #print(e)
    e1 = Emap[e]
    if(Dmap.__contains__(e)):
        d1 = Dmap[e]
        s += min(e1, d1)

print(I, s)