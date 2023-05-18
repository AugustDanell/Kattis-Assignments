# 668th Kattis. A solution to the problem: https://open.kattis.com/problems/bing
N = int(input())
wordlist = {}
for _ in range(N):
    word = input()
    for i in range(1,len(word)+1):
        substring = word[0:i]
        if substring in wordlist:
            wordlist[substring] += 1
        else:
            wordlist[substring] = 0

    print(wordlist[word])
