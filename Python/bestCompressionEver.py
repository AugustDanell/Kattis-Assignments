data = input().split()
N = int(data[0])
b = int(data[1])

if(N < 2**(b+1)):
    print("yes")
else:
    print("no")