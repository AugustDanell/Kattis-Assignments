# Problem Description: https://open.kattis.com/problems/areyoulistening
import math


def euclideanDist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


if __name__ == "__main__":
    x,y, N = list(map(int, input().split()))
    data = []
    for _ in range(N):
        xi, yi, r = list(map(int, input().split()))
        dist = euclideanDist(x,y,xi,yi)
        detection = dist-r
        data.append(detection)

    detectionList = sorted(data)
    print(max(int(detectionList[2]), 0))
