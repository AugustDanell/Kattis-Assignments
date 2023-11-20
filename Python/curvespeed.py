import math
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        R, S = list(map(float, line.split()))
        top = R*(S+.16)
        bot = .067
        print(round(math.sqrt(top / bot)))