data = input()
split = data.split()
# Solution to das blinkenlights.

l1 = int(split[0])
l2 = int(split[1])
seconds = int(split[2])

highBlink = 0
lowBlink = 0

if(l1 > l2):
    highBlink = l1
    lowBlink = l2
else:
    lowBlink = l1
    highBlink = l2

i = 1
factor = lowBlink

while((factor < highBlink) or (not(factor % highBlink == 0))):
    i = i+1
    factor = lowBlink*i

if(factor <= seconds):
    print("yes")
else:
    print("no")