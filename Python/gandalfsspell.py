# Kattis Solution to: https://open.kattis.com/problems/gandalfsspell

# A) Input:
mappingStr = list(input())
wordMap = {}
wordContain = {}
isUnique = True
index = 0
words = input().split()

# B) Match keys and words:
for word in words:
    # 1. Extract the key:
    key = mappingStr[index%len(mappingStr)]

    # 2. Check if the word is old. If it is, check if it maps to the same key:
    if wordContain.__contains__(word) and not wordContain[word] == key:
        isUnique = False
        break
    wordContain[word] = key

    # 3. Check if the key exists and if it maps to the word:
    if not wordMap.__contains__(key):
        wordMap[key] = word
    elif wordMap[key] == word:
        pass
    else:
        isUnique = False
        break

    index += 1

# C) A last special case, if there are empty keys, print False. Else print True, provided that isUnique still holds True:
if isUnique and len(mappingStr) <= len(words):
    print("True")
else:
    print("False")
