# Problem Description: https://open.kattis.com/problems/ummcode

'''
    General Solution:
    Note: Sloopy solution, this is.
    1. Read in every character of the text that is an alpha numeric character.
    2. If a word consists only of u/m, load them into a list, using a boolean expression to make the list basically a binary string.
    3. Chunk the binary string into lengths of 7.
    4. Use map to map every bin-str of length 7 to the binToDec, which will use the binary system to calculate a decimal value.
    5. Use map to map every decimal value to its corresponding ascii value.
    6. Print the contents of the map.
'''

def binToDec(l):
    dec = 0
    for i in range(7):
        if l[::-1][i] == 1:
            dec += 2**i
    return dec



if __name__ == "__main__":
    text = input()
    handledText = []
    for letter in text:
        if letter.isalnum() or letter == " ":
            handledText.append(letter)

    words = "".join(handledText).split()
    binary = []
    for word in words:
        code = True
        for letter in word:
            if letter not in ["u", "m"]:
                code = False
                break
        if code:
            for letter in word:
                binary.append(int(letter == "u"))

    #print(binary, len(binary))
    binaryCells = []
    binaryChunk = []
    while len(binary) > 0:
        if len(binaryChunk) == 7:
            binaryCells.append(binaryChunk[::-1])
            binaryChunk = []
        binaryChunk.append(binary.pop())
    if len(binaryChunk) == 7:
        binaryCells.append(binaryChunk[::-1])

    #print(binaryCells)
    asciiDecimals = list(map(binToDec, binaryCells))
    word = "".join(list(map(chr, asciiDecimals)))
    print(word[::-1])
