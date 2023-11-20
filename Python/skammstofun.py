if __name__ == "__main__":
    N = int(input())
    wordList = input().split()
    abbreviation = ""
    for word in wordList:
        if 65 <= ord(word[0]) <= 92:
            abbreviation += word[0]

    print(abbreviation)