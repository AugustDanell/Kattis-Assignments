import sys

def euclidean(x1,y1,x2,y2):
    return (((x1-x2)**2) + (y1-y2)**2)**(1/2)


def calculate(gx,gy,dx,dy,l):
    gopherDead = True
    for d in l:
        #print(d)
        dogEuclidean = euclidean(dx,dy,d[0],d[1]) / 2
        gopherEuclidean = euclidean(gx,gy,d[0],d[1])

        if(gopherEuclidean < dogEuclidean):
            #print("          The gopher can escape through the hole at (2.500,2.500).")
            print("          The Gopher can escape through the hole at (%f,%f)." %(d[0], d[1]))
            gopherDead = False

    if(gopherDead):
        print("The gopher cannot escape.")


inp = input()
split = inp.split()
gopherX = float(split[0])
gopherY = float(split[1])
dogX = float(split[2])
dogY = float(split[3])

holes = []
for line in sys.stdin:
    split2 = line.split()
    holes.append([float(split2[0]), float(split2[1])])

calculate(gopherX,gopherY,dogX,dogY,holes)