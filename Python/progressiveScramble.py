#Solution to: https://open.kattis.com/problems/progressivescramble

# Takes in a number and spits out a corrosponding ascii chr:
def numVal(n):
    if n == 0:
        return " "
    else:
        return chr(n+96)

# Ditto but in reverse:
def charVal(c):
    if c == " ":
        return 0
    else:
        return ord(c) - 96

# Encrypts a plain text according to the spec:
def encryption(plaintext):
    cryptoText = []
    s = 0
    for element in plaintext:
        s += charVal(element)
        cryptoText.append(s%27)

    cryptoText = list(map(numVal, cryptoText))
    return "".join(cryptoText)


# Ditto but decryption instead:
def decryption(cryptotext):
    cryptotext = list(map(charVal, cryptotext))
    plaintext = [cryptotext[0]]
    prev = cryptotext[0]
    rolls = 0

    # Convert into u_i:
    for i in range(1, len(cryptotext)):
        current = cryptotext[i]
        if current < prev:
            rolls += 1

        plaintext.append(current + (rolls*27))
        prev = current

    temp = plaintext[0]
    # Now we deal with the sum:
    for i in range(1, len(plaintext)):
        tmp = plaintext[i]
        plaintext[i] -= temp
        temp = tmp

    #print(plaintext)

    plaintext = list(map(numVal, plaintext))

    return "".join(plaintext)

# User input, split the string so we have an op part and a text part. Depending on op, text can be plain text or crypto text:
testcases = int(input())
for i in range(testcases):
    s = input()
    op = s[:1]
    text = s[2:]
    
    # Print the answer of either an encryption or a decryption:
    if(op == "e"):
        print(encryption(text))
    else:
        print(decryption(text))
