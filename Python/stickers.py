data = input()
split = data.split()
# Kattis Problem : Laptop Stickers

wc = int(split[0])
hc = int(split[1])
ws = int(split[2])
hs = int(split[3])

if((wc-2) >= ws and (hc-2) >= hs):
    print(1)
else:
    print(0)