def bestOffset(datapoints):
    # Since k = 1, we find the best offset
    # m in kx + m = x + m, or x + a.

    yOffset = 0.0
    N = len(datapoints)
    for datapoint in datapoints:
        x = datapoint[0]
        y = datapoint[1]
        yOffset = yOffset + y-x

    return yOffset/N

def leastSquareLine(datapoints):
    xy = 0
    x = 0
    y = 0
    x2 = 0
    N = len(datapoints)

    for d in datapoints:
        x = x + d[0]
        y = y + d[1]
        x2 = x2 + d[0]*d[0]
        xy = xy + d[0]*d[1]

    m = (N*(xy) - (x)*y) / (N*x2 - (x*x))
    b = (y - m*x)/N
    # m och b => ok
    return [m, b]

testcases = int (input())
datapoints = []
for i in range(testcases):
    datapoint = input().split()
    x = int(datapoint[0])
    y = int(datapoint[1])
    datapoints.append([x,y])

y = bestOffset(datapoints)
print(y)