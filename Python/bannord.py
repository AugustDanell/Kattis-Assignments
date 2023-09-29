letterHash = {}
letterInput = input()
for letter in letterInput:
    letterHash[letter] = True

handledWords = []
words = input().split()
for word in words:
    flaggedWord = False
    for letter in word:
        if(letter in letterHash):
            flaggedWord = True
            break
    
    if(flaggedWord):
        handledWords.append("*"*len(word))
    else:
        handledWords.append(word)

print(" ".join(handledWords))