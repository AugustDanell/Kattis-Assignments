data = input()
split = data.split()

ints = int(split[0])
speedUp = int(split[1])
end = int(split[2])
start = 0

data = input()
points = data.split()

x = end
length = 0.
inc = float(speedUp)/100 # Into percentage
for i in range (ints):
    xNew = int(points[-1 -i])
    length = length + (x-xNew)*(1 + (inc*(ints-i)))
    x = xNew

length = length + (x)
print(length)