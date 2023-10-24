# Problem Description: 

'''
    General Solution:
    We can think of 4 and 7 similar to 1 and 0.
    A) First we can put ourselves in an exponential range, i.e, we can know
    that with two digits we can have 2^2 = 4 combinations, 2^3 = 8 with 3 digits etc.
    We can reduce the number N to be contained within an interval.
    
    B) Once that interval is discerned we can find our lucky number by composing it
    into a bit string of a specific length and lastly we then map 0 -> 4 and 1 -> 7.
'''


# B) A function that produces the Nth lucky number
def getNumber(digits, N):
    
    # 1. Get the corresponding bit string for a range:
    binStr = bin(N)[2:]
    while len(binStr) < digits:
        binStr = "0" + binStr

    # 2. Map 1 -> 7 and 0 -> 4 onto a list:
    newNumber = []
    for digit in binStr:
        if digit == "0":
            newNumber.append("4")
        else:
            newNumber.append("7")
            
    # 3. Return a joined string of the list:
    return "".join(newNumber)

# A) Driver code:
if __name__ == "__main__":
    N = int(input()) -1
    digits = 1
    exp = 1
    while N >= 2**exp:
        N -= 2**exp
        exp += 1
        digits += 1

    print(getNumber(digits, N))
