import sys

shift = 0
for line in sys.stdin:
    data = line.split()
    #print(data)
    if(data == []):
        shift = 0
        print()
    else:
        logs = data[0].count("*")
        data[0] = data[0].replace("*",".")
        data[0] = list (data[0])

        for i in range(1,logs+1):
            data[0][-i-shift] = "*"

        shift += logs
        print("".join(data[0]))