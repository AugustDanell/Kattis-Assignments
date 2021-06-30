import math

def eulcideanDist(a,b):
    ax = a[0]
    ay = a[1]

    bx = b[0]
    by = b[1]

    return math.sqrt((ax-bx)**2 + (ay - by)**2)

data = input().split()

A = [int(data[0]), int(data[1])]

data = input().split()

B = [int(data[0]), int(data[1])]

data = input().split()
C = [int(data[0]), int(data[1])]

h = A
k1 = B
k2 = C
D = eulcideanDist(B,C)

d = eulcideanDist(A,B)
if(d > D):
    h = C
    D = d
    k1 = A
    k2 = B

d = eulcideanDist(A,C)
if(d > D):
    h = B
    D = d
    k1 = A
    k2 = C

# Now we know which points correspond to the hypothenus, saved in h and the distance
# is D (Non important for our solution at hand).

# Stage 2: We want to apply the vector AB to find BE etc:
# We find the vector V(h,k1):

V1 = [k1[0] - h[0], k1[1] - h[1]]
V2 = [k2[0] - h[0], k2[1] - h[1]]

E1 = [k2[0] + V1[0], k2[1] + V1[1]]
E2 = [k1[0] + V2[0], k1[1] + V2[1]]

print(E1[0], E1[1])
#print(E1, E2)