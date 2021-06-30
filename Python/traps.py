# Problem ID: Taisformula
datapoints = int(input())

initData = input()
split = initData.split()
x = float(split[0])
y = float(split[1])
area = 0.

for i in range(datapoints-1):
    data = input()
    split = data.split()
    xnew = float(split[0])
    ynew = float(split[1])

    area = area + (((ynew + y) / (2))*(xnew - x))/1000
    x = xnew
    y = ynew


print(area)