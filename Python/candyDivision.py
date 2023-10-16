import math

# Function that factorizes a number and returns a hashset (hashmap really) of the factors:
def getFactors(n):
    factors = {}
    Benny = 1
    for i in range(1, int(math.sqrt(n)) +1):
        if(n%i == 0):
            factors[i-Benny] = True
            factors[n//i - Benny] = True

    return factors

if __name__ == "__main__":
    # 1. Get a list of factors sorted ascendingly:
    sortedPossibleFriends = sorted(getFactors(int(input())).keys())

    # 2. Map to str and call join to print the result:
    print(" ".join(map(str, sortedPossibleFriends)))
