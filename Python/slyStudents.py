# https://open.kattis.com/problems/slystudents

import math

# A function that converts decimals to ternary form:
def decToTernary(n):
    ternaryList = []
    while n > 0:
        remainder = n % 3
        n //= 3
        ternaryList.append(str(remainder))

    return ("".join(ternaryList[::-1]))

# A function that finds decimal factors of n:
def findFactors(n):
    factors = {}
    for i in range(1, int(math.sqrt(n))+1):
        if(n%i == 0):
            factors[n//i] = True
            factors[i] = True
    return factors

# A function that finds all factors that every character has in common:
def commonFactors(word):
    oldFactors = findFactors(ord(word[0]))
    for i in range (1, len(word)):
        newFactors = findFactors(ord(word[i]))
        commonFactors = {}
        for newFactor in newFactors:
            if newFactor in oldFactors:
                commonFactors[newFactor] = True
        oldFactors = {}
        for commonFactor in commonFactors:
            oldFactors[commonFactor] = True
    return oldFactors

# The main function:
def encryptWord(word):

    # 1. Get the max common factor for every char:
    maxFactor = sorted(list(commonFactors(word)), reverse=True)[0]
    
    # 2. Convert each word to ASCII-int and divide with the max factor:
    numericList = list(map(ord, word))
    for i in range(len(numericList)):
        numericList[i] //=maxFactor

    # 3. Create a ternary list for every word:
    ternaryList = map(decToTernary, numericList)

    # 4. Print the max factor and the joined ternaryList:
    print(maxFactor)
    print(" ".join(ternaryList))

if __name__ == "__main__":

    # 0. Some tests:
    test = True
    if test:
        assert(5 in commonFactors("Fix"))
        assert(decToTernary(14) == "112")
        assert (decToTernary(21) == "210")
        assert (decToTernary(24) == "220")

    # 1. Feed every individual word to the de-facto main function (encryptWord)
    inputStr = input().split()
    for word in inputStr:
        encryptWord(word)
