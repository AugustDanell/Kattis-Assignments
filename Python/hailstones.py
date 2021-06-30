# Problem ID: hailstone
def hailStone(n):
    if(n == 1):
        return 1
    elif(n%2 == 0):
        return n + hailStone(n//2)
    else:
        return n + hailStone(n*3 + 1)

start = int(input())

print(hailStone(start))