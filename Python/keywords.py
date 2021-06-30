def removeHyphens(word):
    for i in range(len(word)):
        if(word[i] == "-"):
            word[i] = " "

    return word

words = int(input())
wordList = {}
notSame = 0

for i in range(words):
    word = list (input().lower())
    word = removeHyphens(word)
    phrase = "".join(word)
    if(not wordList.__contains__(phrase)):
        wordList[phrase] = phrase
        notSame = notSame +1

print(notSame)
