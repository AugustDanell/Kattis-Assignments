# Solution to the problem: https://open.kattis.com/problems/goodmessages

def okForBoris(l):
    # Checks a list l if it matches Boris requirements pertaining to vowels:
    vowelcounter = 0
    consonantcounter = 0
    for c in l:
        if c in ["a", "e", "i", "o", "u", "y"]:
            vowelcounter += 1
        else:
            consonantcounter += 1

    return consonantcounter > 2*vowelcounter

assert okForBoris(list("fef")) == False

def chrToNum(c):
    # Converts a character to a lower case mapping [a, z] -> [0, 25]:
    return ord(c) - 97

assert chrToNum("a") == 0
assert chrToNum("z") == 25

def numToChr(n):
    # Inversely converts a number to a character [0, 25] -> [a, z], defined in the congruency group Z_25:
    n %= 26
    return chr(n + 97)

assert (numToChr(chrToNum("a"))) == "a"
assert (chrToNum(numToChr(10+26))) == 10

def ceasarCypher(key, l):
    # Apply the ceasar cypher with a specified key and a plaintext stored in the list l:
    cypherText = []
    for character in l:
        num = chrToNum(character)
        newNum = (num + key)%26
        cryptoChr = numToChr(newNum)
        cypherText.append(cryptoChr)
    return cypherText

assert ceasarCypher(2, ["a"]) == ["c"]
assert ceasarCypher(25, ["a"]) == ["z"]
assert ceasarCypher(26, ["a","b","c"]) == ["a", "b", "c"]
assert ceasarCypher(2, ["y"]) == ["a"]

# 1. Take in the input:
offset = (int(input()))%26
plaintext = list(input())
iterations = int(input())
cryptoText = plaintext
Boris = 0

# 2. Iterate over how many iterations we have and transform cryptotext iteratively:
for _ in range(iterations):
    cryptoText = ceasarCypher(offset, cryptoText)

    # 3. Validate the cryptotext. If not valid, increment the counter:
    if okForBoris(cryptoText):
        Boris += 1

    #print(cryptoText)

# 4. Let the counter define a ratio:
okRatio = Boris / iterations

# 5. Depending on the ratio of valid outputs, output the correct answer:
if okRatio > 0.5:
    print("Boris")
else:
    print("Colleague")
