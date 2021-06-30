import math
def generateWord(n):
    word = ""
    wordList = []
    a = int(math.log(n, 25))
    while(n > 0):
        d = int (n/25**a)
        #word = word.join(chr(97+d))
        #word += (chr(97+d))
        wordList.append(chr(97+d))
        n -= d*25**a
        a-=1

    return word.join(wordList) + " "

data = input().split()
mini = int(data[0])
maxi = int(data[1])

#print(generateWord(25))
#print(generateWord(30))
#print(generateWord(40))
#print(generateWord(50))

n = 1
s = ""
l = []
for i in range(maxi):
    l.append(generateWord(n))
    n += 1

print("".join(l))