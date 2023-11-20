import math
import sys

def isPrime(N):
    if N < 2:
        return False

    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

if __name__ == "__main__":
    answers = []
    failed = False
    for line in sys.stdin:
        data = line.strip().split()
        if len(data) > 0:
            for item in data:
                try:
                    if str(int(item)) != item:
                        raise Exception

                    answers.append(int(item))
                except:
                    failed = True

    if not len(answers) == 3 or failed:
        print(0)
    else:
        a, b, c = answers
        if (a < 3) or (a > 10 ** 9) or (a%2 == 1):
            failed = True

        if b + c == a and isPrime(b) and isPrime(c) and not failed:
            print(1)
        else:
            print(0)