import math
def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number%i == 0:
            print((int((i-1)*number/i)))
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    if is_prime(n):
        print(n-1)
