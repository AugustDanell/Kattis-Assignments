import math

def isPrime(N):
    for div in range(int(math.sqrt(N)) +1):
        if N % div == 0:
            return False
    return True
def timesDivisible(div, N):
    times = 0
    while N % div == 0:
        times += 1
        N //= div
    return times

def getFactors(N):
    factors = []
    for div in range(2, int(math.sqrt(N))+1):
        if N % div == 0:
            times = timesDivisible(div, N)
            factors.append([div, times])
    return factors

if __name__ == "__main__":
    fizzes = {}
    buzzes = {}
    start, end = list(map(int,input().split()))
    startFizz = -1
    startBuzz = -1
    ansFizz = -1
    ansBuzz = -1

    numbers = input().split()
    for i in range(len(numbers)):
        number = numbers[i]
        orderedNumber = start + i

        # Set Fizz and buzzes:
        fizz = False
        buzz = False
        if number == "FizzBuzz":
            fizz = True
            buzz = True
        elif number == "Buzz":
            buzz = True
        elif number == "Fizz":
            fizz = True

        # Deduce exactly via stepsize:
        if startFizz == -1 and fizz:
            startFizz = orderedNumber
        elif ansFizz == -1 and fizz:
            ansFizz = orderedNumber - startFizz
        if startBuzz == -1 and buzz:
            startBuzz = orderedNumber
        elif ansBuzz == -1 and buzz:
            ansBuzz = orderedNumber - startBuzz


    # If only one occurance:
    if ansFizz == -1 and startFizz != -1:
        ansFizz = startFizz
    if ansBuzz == -1 and startBuzz != -1:
        ansBuzz = startBuzz

    length = end - start
    upperSolutions = [x for x in range (end+1, end +3) if x < 10**6]
    lowerSolutions = [x for x in range(start-1, start-length, -1) if x*2 > end]
    
    solutions = lowerSolutions + upperSolutions
    # If no occurance of fizz:
    if len(solutions) > 0:
        if ansFizz == -1:
            ansFizz = solutions[-1]
        if ansBuzz == -1:
            ansBuzz = solutions[-1]


    print(ansFizz, ansBuzz)