# Problem Description: https://open.kattis.com/problems/successfulzoom

if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    increaseMap = {}
    found = False
    for h in range(1, N//2 + 1):
        current = h-1
        localFound = True
        while current + h < N:
            prev = current
            current += h
            if numbers[current] <= numbers[prev]:
                localFound = False
                break

        if localFound:
            print(h)
            found = True
            break

    if not found:
        print("ABORT!")
