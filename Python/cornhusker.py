https://open.kattis.com/problems/cornhusker
if __name__ == "__main__":
    numbers = list(map(int,input().split()))
    total = 0
    for i in range(0, len(numbers), 2):
        total += numbers[i]*numbers[i+1]

    avg = int(total / 5)
    N, K = list(map(int,input().split()))
    print(int(avg*N/K))
